class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        one = nums[0]
        nums[1:] = sorted(nums[1:])
        return one + nums[1] + nums[2]
