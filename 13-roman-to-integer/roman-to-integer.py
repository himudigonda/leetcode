class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for cur, nxt in zip(s, s[1:]):
            if mapping[cur] < mapping[nxt]:
                res -= mapping[cur]
            else:
                res += mapping[cur]
        return res + mapping[s[-1]]
