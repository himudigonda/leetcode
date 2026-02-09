class Solution:
    def minOperations(self, nums: List[int]) -> int:
        curmax = float("-inf")
        count = 0

        for idx in range(1, len(nums)):
            if nums[idx - 1] >= nums[idx]:
                count += nums[idx - 1] - nums[idx] + 1
                nums[idx] = nums[idx - 1] + 1
        return count
