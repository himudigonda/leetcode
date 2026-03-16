class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        evens = (n + 1) // 2
        odds = n // 2

        def find_pow(x, n):
            if n == 0:
                return 1
            ans = find_pow(x, n // 2)
            ans *= ans
            ans %= MOD
            if n % 2:
                ans *= x
            ans %= MOD
            return ans

        # res = ((5 ** evens) * (4 ** odds)) % ((10 ** 9) + 7)
        # res = (pow(5, evens, MOD) * pow(4, odds, MOD)) % MOD
        res = (find_pow(5, evens) * find_pow(4, odds)) % MOD
        return res
