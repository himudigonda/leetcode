class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            # returns 1 after clearing the island
            if (
                row >= ROWS
                or col >= COLS
                or row < 0
                or col < 0
                or grid[row][col] != "1"
            ):
                return
            grid[row][col] = "0"
            dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in dirs:
                dfs(row + dr, col + dc)
            return

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
