class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums.sort()
        left = 0
        right = len(nums) - 1


        maxsum = 0
        while left < right:
            maxsum = max(maxsum, nums[left] + nums[right])
            left += 1
            right -= 1
        return maxsum
