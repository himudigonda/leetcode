class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx, val in enumerate(nums):
            if idx == val:
                continue
            else:
                return idx
        return idx + 1
