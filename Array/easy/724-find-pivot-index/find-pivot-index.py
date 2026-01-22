class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for idx, num in enumerate(nums):
            left += num
            if left == right:
                return idx
            right -= num
        return -1