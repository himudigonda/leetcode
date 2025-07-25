class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        if len(nums) == 1:
            return nums[0]

        if max(nums) < 0:
            return max(nums)

        for i in sett:
            res += i if i > 0 else 0
        return res
