class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Brute Force TLE
        def findDivisors(num):
            res = []
            limit = num ** 0.5
            i = 1
            while i <= limit:
                if num % i == 0:
                    res.append(i)
                    posdiv = num // i
                    if posdiv != i:
                        res.append(posdiv)
                i += 1
            return res
        #     for i in range(1, num // 2 + 1):
        #         if num % i == 0:
        #             res.append(i)
        #     return res + [num]

        res = 0
        for num in nums:
            divisors = findDivisors(num)
            if len(divisors) != 4:
                continue
            res += sum(divisors)
        return res
