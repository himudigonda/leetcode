class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCounts = Counter(s)
        tCounts = Counter(t)

        for i in sCounts:
            if tCounts[i] == sCounts[i]:
                continue
            else:
                return False
        return True