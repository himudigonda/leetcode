class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        idx = 0
        n = len(s)
        for ch in s:
            if int(ch) == idx:
                count += 1
            idx ^= 1

        return min(count, n - count)
