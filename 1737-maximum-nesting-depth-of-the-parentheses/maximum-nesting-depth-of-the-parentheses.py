class Solution:
    def maxDepth(self, s: str) -> int:
        ptr = 0
        res = 0
        maxres = 0
        for ptr in range(len(s)):
            if s[ptr] == "(":
                res += 1
            elif s[ptr] == ")":
                res -= 1
            maxres = max(res, maxres)
        return maxres
