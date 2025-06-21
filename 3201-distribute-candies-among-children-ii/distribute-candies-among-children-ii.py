class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def combinations(k):
            # Calculates C(k + 2, 2) for non-negative k
            if k < 0:
                return 0
            return (k + 2) * (k + 1) // 2

        # Total ways without any limit
        total_ways = combinations(n)

        # S1: Cases where at least one child exceeds the limit
        s1 = 3 * combinations(n - (limit + 1))

        # S2: Cases where at least two children exceed the limit
        s2 = 3 * combinations(n - 2 * (limit + 1))

        # S3: Cases where all three children exceed the limit
        s3 = combinations(n - 3 * (limit + 1))

        ans = total_ways - s1 + s2 - s3
        return ans
