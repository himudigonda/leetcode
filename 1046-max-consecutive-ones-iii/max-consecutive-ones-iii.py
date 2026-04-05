class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left, maxlen, zeros = 0, 0, 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            # maxlen = max(maxlen, right - left + 1)
        return len(nums) - left
