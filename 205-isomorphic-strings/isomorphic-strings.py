class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}

        for ss, tt in zip(s, t):
            if ss in s2t:
                if s2t[ss] != tt:
                    return False
            elif tt in t2s:
                return False
            s2t[ss] = tt
            t2s[tt] = ss
        return True
