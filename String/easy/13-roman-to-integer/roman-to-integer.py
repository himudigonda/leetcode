class Solution:
    def romanToInt(self, s: str) -> int:
        # Base Implementation
        # res = 0
        # mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # for cur, nxt in zip(s, s[1:]):
        #     if mapping[cur] < mapping[nxt]:
        #         res -= mapping[cur]
        #     else:
        #         res += mapping[cur]
        # return res + mapping[s[-1]]

        # Slightly Optimized Implementation
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = 0
        total = 0

        for char in reversed(s):
            cur = mapping[char]
            if cur < prev:
                total -= cur
            else:
                total += cur
            prev = cur
        return total
