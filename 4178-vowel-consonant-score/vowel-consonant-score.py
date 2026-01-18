class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vo = set(["a", "e", "i", "o", "u"])
        vscore = 0
        cscore = 0
        for ch in s:
            if ch.isalpha():
                if ch in vo:
                    vscore += 1
                else:
                    cscore += 1
        return floor(vscore / cscore) if cscore else 0
