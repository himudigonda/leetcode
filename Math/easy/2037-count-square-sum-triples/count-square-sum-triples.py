class Solution:
    def countTriples(self, n: int) -> int:
        # # BruteForce
        # count = 0
        # for i in range(1, n):
        #     for j in range(i + 1, n):
        #         c_sq = i * i + j * j
        #         c = int(sqrt(c_sq))

        #         if c * c == c_sq and c <= n:
        #             count += 2
        # return count

        # Optimal using math
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = 0
        i = 0
        while i * i < n:
            for j in range(1, i):
                if gcd(i, j) == 1 and (i - j) % 2 == 1:
                    c_prim = i * i + j * j
                    if c_prim > n:
                        break

                    count += 2 * (n // c_prim)
            i += 1
        return count
