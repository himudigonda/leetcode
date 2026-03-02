class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        mid = 0
        right = len(nums) - 1
        if len(nums) == 1: return nums

        # while left < len(nums) and nums[left] == 0:
        #     left += 1
        # mid = left + 1
        # while nums[right] == 2:
        #     right -= 1

        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        return nums
