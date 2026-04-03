class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = len(nums) - 2
        while ptr >= 0 and nums[ptr] >= nums[ptr + 1]:
            ptr -= 1

        if ptr >= 0:
            target = len(nums) - 1
            while nums[target] <= nums[ptr]:
                target -= 1
            nums[target], nums[ptr] = nums[ptr], nums[target]

        end = len(nums) - 1
        ptr += 1
        while ptr < end:
            nums[ptr], nums[end] = nums[end], nums[ptr]
            ptr += 1
            end -= 1
        return nums
