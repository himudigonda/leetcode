class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        main = 0
        end = len(nums) - 1

        while main <= end:
            if nums[main] == 0:
                nums[main], nums[zero] = nums[zero], nums[main]
                main += 1
                zero += 1
            elif nums[main] == 1:
                main += 1
            else:
                nums[main], nums[end] = nums[end], nums[main]
                end -= 1
        return nums
