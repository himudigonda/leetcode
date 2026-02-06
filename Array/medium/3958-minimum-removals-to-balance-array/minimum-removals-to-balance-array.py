class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_kept = 0

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            size = right - left + 1
            max_kept = max(max_kept, size)
        return n - max_kept
