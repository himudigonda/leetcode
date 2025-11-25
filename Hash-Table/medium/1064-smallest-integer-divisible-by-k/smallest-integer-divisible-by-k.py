class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r = 0
        for c in range(1, k + 1):
            r = (r * 10 + 1) % k
            if r == 0: return c
        return -1