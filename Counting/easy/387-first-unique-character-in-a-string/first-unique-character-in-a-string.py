class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for idx in range(len(s)):
            if counts[s[idx]] == 1:
                return idx
        return -1
