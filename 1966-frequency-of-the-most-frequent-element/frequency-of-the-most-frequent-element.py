class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # BruteForce
        nums.sort()
        l = 0
        total = 0
        res = 1

        for r in range(1, len(nums)):
            total += (nums[r] - nums[r - 1]) * (r - l)
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
