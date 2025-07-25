class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sett = set()
        left = 0
        val = 0
        maxVal = 0
        for right in range(len(nums)):
            while nums[right] in sett:
                sett.remove(nums[left])
                val -= nums[left]
                left += 1
            sett.add(nums[right])
            val += nums[right]
            maxVal = max(maxVal, val)
        return maxVal
