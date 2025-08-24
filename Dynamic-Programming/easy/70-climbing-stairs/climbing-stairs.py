class Solution:
    def climbStairs(self, n: int) -> int:
        # # Brute Force
        # counts = [1] * n
        # if n > 1:
        #     counts[1] = 2
        # for i in range(2, n):
        #     counts[i] = counts[i - 2] + counts[i - 1]
        # return counts[-1]

        # Optimal
        if n == 0 or n == 1:
            return 1
        prev = 1
        nextt = 1
        for i in range(2, n + 1):
            temp = nextt
            nextt = nextt + prev
            prev = temp
        return nextt
