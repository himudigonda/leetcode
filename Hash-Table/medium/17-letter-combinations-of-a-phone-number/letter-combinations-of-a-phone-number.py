class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

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
        result = []

        def backtracking(i, currstr):
            if i == len(digits):
                result.append(currstr)
                return

            digit = digits[i]
            letters = mapping[digit]
            for letter in letters:
                backtracking(i + 1, currstr + letter)

        backtracking(0, "")
        return result
