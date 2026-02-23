class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = set()
        s = list(s)
        for i in range(len(s) - k + 1):
            string = s[i : i + k]
            res.add(''.join(string))
            if len(res) == 2**k:
                return True

        return False
