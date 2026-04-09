class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or board[r][c] != 'O':
                return
            
            board[r][c] = '_'
            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                newr, newc = r + dr, c + dc
                dfs(newr, newc)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
                
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "_":
                    board[r][c] = "O"

        return board
