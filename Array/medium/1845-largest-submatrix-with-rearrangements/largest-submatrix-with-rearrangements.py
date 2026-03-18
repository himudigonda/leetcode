class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # height = [0] * COLS
        # ans = 0

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == 1:
        #             height[j] += 1
        #         else:
        #             height[j] = 0

        #     cheight = sorted(height, reverse=True)
        #     for j in range(COLS):
        #         ans = max(ans, (j + 1) * cheight[j])
        # return ans
        ROWS = len(matrix)
        COLS = len(matrix[0])
        prev = [0] * COLS
        ans = 0

        for i in range(ROWS):
            cur = matrix[i]
            for j in range(COLS):
                if cur[j] == 1:
                    cur[j] += prev[j]

            ccur = sorted(cur, reverse=True)
            for j in range(COLS):
                ans = max(ans, (j + 1) * ccur[j])
            prev = cur
        return ans
