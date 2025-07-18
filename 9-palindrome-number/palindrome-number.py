class Solution:
    def isPalindrome(self, x: int) -> bool:
        # # BruteForce
        # if x < 0:
        #     return False
        # s = str(x)
        # reversed_s = s[::-1]
        # return s == reversed_s

        # Optimal
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            last_digit = x % 10
            reverted_number = reverted_number * 10 + last_digit
            x //= 10
        return x == reverted_number or x == reverted_number // 10