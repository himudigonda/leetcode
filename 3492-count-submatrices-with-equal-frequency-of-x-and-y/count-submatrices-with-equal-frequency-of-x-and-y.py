class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        curSumX = [[0] * COLS for _ in range(ROWS)]
        curSumY = [[0] * COLS for _ in range(ROWS)]

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                curSumX[i][j]  = grid[i][j] == 'X'
                curSumY[i][j]  = grid[i][j] == 'Y'

                if i - 1 >= 0:
                    curSumX[i][j] += curSumX[i - 1][j]
                    curSumY[i][j] += curSumY[i - 1][j]
                if j - 1 >= 0:
                    curSumX[i][j] += curSumX[i][j - 1]
                    curSumY[i][j] += curSumY[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    curSumX[i][j] -= curSumX[i - 1][j - 1]
                    curSumY[i][j] -= curSumY[i - 1][j - 1]
                
                if curSumX[i][j] and curSumX[i][j] == curSumY[i][j]:
                    count += 1
        return count