class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        curprod = 1
        res = 0
        for right in range(len(nums)):
            curprod *= nums[right]
            while left <= right and curprod >= k:
                curprod /= nums[left]
                left += 1
            res += right - left + 1
        return res
