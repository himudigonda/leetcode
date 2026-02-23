class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = set()
        for i in range(len(s) - k + 1):
            string = s[i : i + k]
            res.add(string)
            if len(res) == 2**k:
                return True

        return False
