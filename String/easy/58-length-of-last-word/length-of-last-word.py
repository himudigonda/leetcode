class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        index = len(s) - 1
        res = 0

        while s[index] == " ":
            index -= 1

        while index >= 0 and s[index] != " ":
            res += 1
            index -= 1

        return res
