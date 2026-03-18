class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        if not digits:
            return []

        def dfs(idx, curarr):
            # if len(curarr) == len(digits):
            if idx == len(digits):
                res.append("".join(curarr))
                return

            possibles = mapping[digits[idx]]
            for ch in possibles:
                curarr.append(ch)
                dfs(idx + 1, curarr)
                curarr.pop()
            return

        dfs(0, [])
        return res
