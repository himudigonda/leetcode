class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scounter = Counter(s)
        tcounter = Counter(t)
        # print(scounter, tcounter)
        count = 0

        for c in scounter:
            if scounter[c] > tcounter[c]:
                count += scounter[c] - tcounter[c]
        return count
