class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum = sum(stones)
        target = totalsum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for s in range(target, stone - 1, -1):
                if dp[s - stone]:
                    dp[s] = True

        maxsum = 0
        for s in range(target, -1, -1):
            if dp[s]:
                maxsum = s
                break

        return totalsum - 2 * maxsum