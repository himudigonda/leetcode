class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        curSumX = [0] * COLS
        curSumY = [0] * COLS
        # curSumX = [[0] * COLS for _ in range(ROWS)]
        # curSumY = [[0] * COLS for _ in range(ROWS)]

        count = 0

        for r in range(ROWS):
            curx, cury = 0, 0
            for c in range(COLS):
                if grid[r][c] == "X":
                    curx += 1
                elif grid[r][c] == "Y":
                    cury += 1
                curSumX[c] += curx
                curSumY[c] += cury
                if curSumX[c] == curSumY[c] and curSumX[c]:
                    count += 1
        return count

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         curSumX[i][j]  = grid[i][j] == 'X'
        #         curSumY[i][j]  = grid[i][j] == 'Y'

        #         if i - 1 >= 0:
        #             curSumX[i][j] += curSumX[i - 1][j]
        #             curSumY[i][j] += curSumY[i - 1][j]
        #         if j - 1 >= 0:
        #             curSumX[i][j] += curSumX[i][j - 1]
        #             curSumY[i][j] += curSumY[i][j - 1]
        #         if i - 1 >= 0 and j - 1 >= 0:
        #             curSumX[i][j] -= curSumX[i - 1][j - 1]
        #             curSumY[i][j] -= curSumY[i - 1][j - 1]

        #         if curSumX[i][j] and curSumX[i][j] == curSumY[i][j]:
        #             count += 1
        # return count
