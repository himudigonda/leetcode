class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)

        res = []
        for idx, num in enumerate(nums):
            right -= num
            res.append(abs(right - left))
            left += num
        return res
