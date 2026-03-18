class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        temp = [[0] * (COLS + 1) for i in range(ROWS + 1)]

        for i in range(ROWS):
            for j in range(COLS):
                temp[i + 1][j + 1] = (
                    grid[i][j] + temp[i][j + 1] + temp[i + 1][j] - temp[i][j]
                )
                if temp[i + 1][j + 1] <= k:
                    res += 1
                else:
                    break
        return res
        