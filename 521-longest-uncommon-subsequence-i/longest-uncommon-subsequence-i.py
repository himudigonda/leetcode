class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        countsA = Counter(a)
        countsB = Counter(b)
        resA = 0
        resB = 0

        for key, val in countsA.items():
            if key not in set(countsB.items()):
                resA += val

        for key, val in countsB.items():
            if key not in set(countsB.items()):
                resB += val

        return max(resA, resB) if resA and resB else -1
