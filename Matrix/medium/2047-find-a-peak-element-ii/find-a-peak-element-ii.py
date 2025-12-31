class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # def checkIfPeak(x, y):
        #     if x > -1 and y > -1 and x < len(mat) and y < len(mat[0]):
        #         left = mat[x][y - 1] if y > 1 else 0
        #         right = mat[x][y + 1] if y < len(mat[0]) - 1 else 0
        #         top = mat[x - 1][y] if x > 1 else 0
        #         bottom = mat[x + 1][y] if x < len(mat) - 1 else 0
        #         if mat[x][y] > max(left, right, top, bottom):
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False

        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if checkIfPeak(i, j):
        #             return [i, j]

        rows = len(mat)
        cols = len(mat[0])
        left = 0
        right = cols - 1

        while left <= right:
            mid = (left + right) // 2
            maxrow = 0
            for r in range(rows):
                if mat[r][mid] > mat[maxrow][mid]:
                    maxrow = r

            left_val = mat[maxrow][mid - 1] if mid > 0 else -1
            right_val = mat[maxrow][mid + 1] if mid < cols - 1 else -1
            cur_val = mat[maxrow][mid]

            if cur_val > left_val and cur_val > right_val:
                return [maxrow, mid]
            elif cur_val < right_val:
                left = mid + 1
            else:
                right = mid - 1
        return []
