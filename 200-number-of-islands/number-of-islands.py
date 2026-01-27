class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if (
                row >= ROWS
                or row < 0
                or col >= COLS
                or col < 0
                or grid[row][col] == "0"
            ):
                return
            grid[row][col] = "0"

            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirs:
                dfs(row + dr, col + dc)

        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
