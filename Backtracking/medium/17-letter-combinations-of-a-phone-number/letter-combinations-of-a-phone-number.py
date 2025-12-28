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
        n = len(digits)
        res = []

        def backtrack(idx, cur):
            if idx >= n:
                res.append(cur[:])
                return
            new_letters = list(mapping[digits[idx]])
            for letter in new_letters:
                backtrack(idx + 1, cur + letter)

        backtrack(0, "")
        return res
