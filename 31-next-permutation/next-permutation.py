class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = len(nums) - 2
        while ptr >= 0 and nums[ptr] >= nums[ptr + 1]:
                ptr -= 1



        if ptr >= 0:
            target_finder = len(nums) - 1
        # while nums[target_finder] <=
            while nums[target_finder] <= nums[ptr]:
                target_finder -= 1
            nums[target_finder], nums[ptr] = nums[ptr], nums[target_finder]
        
    
        end = len(nums) -1 
        ptr += 1
        while ptr < end:
            nums[ptr], nums[end] = nums[end], nums[ptr]
            ptr += 1
            end -= 1
        return nums

        
        # nums[ptr], nums[ptr + 1] = nums[ptr + 1], nums[ptr]
        # nums[ptr + 2 :] = sorted(nums[ptr + 2 :])
        # return nums
