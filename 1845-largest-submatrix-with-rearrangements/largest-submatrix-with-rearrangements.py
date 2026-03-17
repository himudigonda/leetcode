class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(1, ROWS):
            for j in range(COLS):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        ans = 0
        for i in range(ROWS):
            matrix[i].sort(reverse=True)
            for j in range(COLS):
                ans = max(ans, (j + 1) * matrix[i][j])
        return ans
