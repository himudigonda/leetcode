class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        res = 0
        for i in range(k):
            curhappiness = happiness[i] - i
            if curhappiness < 0:
                break
            res += curhappiness
        return res
