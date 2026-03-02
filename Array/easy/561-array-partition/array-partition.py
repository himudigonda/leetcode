class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        res = 0
        for i in range(len(nums) - 1, -1, -2):
            res += nums[i]
        return res
