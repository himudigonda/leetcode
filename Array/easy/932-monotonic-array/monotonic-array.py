class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        order = nums[-1] > nums[0]

        for idx in range(1, len(nums)):
            if order:
                if nums[idx-1] > nums[idx]: return False
            else:
                if nums[idx-1] < nums[idx]: return False
        return True
