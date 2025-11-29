class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[right] == val:
                right += 1
            else:
                nums[left] = nums[right]
                right += 1
                left += 1
        return left