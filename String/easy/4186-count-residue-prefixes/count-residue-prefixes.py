class Solution:
    def residuePrefixes(self, s: str) -> int:
        res, sett = 0, set()
        for idx, char in enumerate(s):
            sett.add(char)
            if len(sett) == (idx + 1) % 3:
                res += 1
            elif len(sett) > 2:
                break
        return res
