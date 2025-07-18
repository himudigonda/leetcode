class Solution:
    def reverse(self, x: int) -> int:
        # # BruteForce
        # MAX_INT = 2**31 - 1
        # MIN_INT = -2**31
        # is_negative = x < 0
        # s = str(abs(x))
        # reversed_s = s[::-1]
        # reversed_val = int(reversed_s)
        # if is_negative:
        #     reversed_val = -reversed_val
        # if reversed_val < MIN_INT or reversed_val > MAX_INT:
        #     return 0
        # return reversed_val

        # Optimal
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1 if x >= 0 else -1
        num = abs(x)
        reversed_num = 0
        limit = INT_MAX if sign == 1 else abs(INT_MIN)
        limit_div_10 = limit // 10
        limit_mod_10 = limit % 10
        while num > 0:
            digit = num % 10
            num //= 10
            if reversed_num > limit_div_10:
                return 0
            if reversed_num == limit_div_10 and digit > limit_mod_10:
                return 0
            reversed_num = reversed_num * 10 + digit
        return reversed_num * sign