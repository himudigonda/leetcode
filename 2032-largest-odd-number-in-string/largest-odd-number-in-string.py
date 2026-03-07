class Solution:
    def largestOddNumber(self, num: str) -> str:
        right = 0
        for right in range(len(num) - 1, -1, -1):
            if int(num[right]) % 2 == 1:
                return num[:right + 1]
            if right == 0: return ""