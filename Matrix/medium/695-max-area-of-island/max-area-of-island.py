class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if row >= ROWS or row < 0 or col >= COLS or col < 0 or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            cursum = 1
            cursum += dfs(row + 1, col)
            cursum += dfs(row, col + 1)
            cursum += dfs(row - 1, col)
            cursum += dfs(row, col - 1)

            return cursum

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
