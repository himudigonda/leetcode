class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            # digits = list(str(n))
            # digits = [int(x) for x in digits]
            # for idx in range(len(digits)):
            #     digits[idx] *= digits[idx]
            # n = sum(digits)
            res = 0
            for i in str(n):
                res += int(i) ** 2
            n = res
        return False
