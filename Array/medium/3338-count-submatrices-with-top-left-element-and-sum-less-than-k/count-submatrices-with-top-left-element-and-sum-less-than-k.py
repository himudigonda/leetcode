class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        # temp = [[0] * (COLS + 1) for i in range(ROWS + 1)]
        temp = [0] * COLS

        for i in range(ROWS):
            prefix_row = 0
            for j in range(COLS):

                # temp[i + 1][j + 1] = (
                #     grid[i][j] + temp[i][j + 1] + temp[i + 1][j] - temp[i][j]
                # )
                prefix_row += grid[i][j]
                temp[j] += prefix_row
                # if temp[i + 1][j + 1] <= k:
                if temp[j] <= k:
                    res += 1
                else:
                    break
        return res
