class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        cursum = 0
        maxsum = nums[0]

        for right in range(len(nums)):
            if cursum < 0:
                left = right + 1
                cursum = 0
            cursum += nums[right]
            maxsum = max(maxsum, cursum)
        return maxsum
