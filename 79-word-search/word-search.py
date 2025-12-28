class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # path = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
                or word[idx] != board[row][col]
                # or (row, col) in path
            ):
                return False

            # path.add((row, col))
            temp = board[row][col]
            board[row][col] = "#"

            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                if dfs(row + dr, col + dc, idx + 1):
                    board[row][col] = temp
                    return True
            # res = (
            #     dfs(row + 1, col, idx + 1)
            #     or dfs(row, col + 1, idx + 1)
            #     or dfs(row - 1, col, idx + 1)
            #     or dfs(row, col - 1, idx + 1)
            # )
            # path.remove((row, col))
            board[row][col] = temp
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
