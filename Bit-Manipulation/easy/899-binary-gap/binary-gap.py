class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        # cur = 0
        maxgap = 0

        # while n > 0:
        for cur in range(32):
            if (n >> cur) & 1:
            # if n & 1:
                if prev != -1:
                    maxgap = max(maxgap, cur - prev)
                prev = cur
            # n >>= 1
            # cur += 1
        return maxgap
