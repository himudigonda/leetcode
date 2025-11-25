class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        orig = x
        res = 0

        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
        return res == orig
