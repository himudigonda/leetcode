class Solution:
    def reverse(self, x: int) -> int:
        sign = None
        if x >= 0:
            sign = True
        else:
            sign = False

        x = abs(x)
        res = 0
        while x >= 1:
            num = x % 10
            x = x // 10
            res = res * 10 + num

        if res > 2**31 or res < (-(2**31)) - 1:
            return 0
        return res * -1 if not sign else res
