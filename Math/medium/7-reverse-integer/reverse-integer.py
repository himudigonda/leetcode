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
        sign = -1 if x < 0 else 1
        x *= sign
        reverse = 0
        while x:
            reverse = reverse * 10 + x % 10
            x //= 10
        if reverse > 2**31 - 1:
            return 0
        return sign * reverse