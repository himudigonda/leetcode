class Solution:
    def minCost(self, n: int) -> int:
        # return n * (n - 1) // 2
        memo = {}

        def solve(x):
            if x == 1:
                return 0
            if x in memo:
                return memo[x]

            mincost = float("inf")

            for i in range(1, x):
                current = i * (x - i)
                net = current + solve(i) + solve(x - i)
                mincost = min(mincost, net)
            memo[x] = mincost
            return mincost

        return solve(n)
