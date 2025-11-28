class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while bottom <= top:
            midrow = (top + bottom) // 2
            if matrix[midrow][left] <= target <= matrix[midrow][right]:
                while left <= right:
                    midcol = (left + right) // 2
                    if matrix[midrow][midcol] == target:
                        return True
                    elif matrix[midrow][midcol] > target:
                        right = midcol - 1
                    else:
                        left = midcol + 1
            elif matrix[midrow][left] > target:
                top = midrow - 1
            else:
                bottom = midrow + 1
        return False