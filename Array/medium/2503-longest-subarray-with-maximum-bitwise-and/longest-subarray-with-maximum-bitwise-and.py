class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxval = max(nums)
        maxlen = 0
        curlen = 0

        for num in nums:
            if num == maxval:
                curlen += 1
            else:
                maxlen = max(maxlen, curlen)
                curlen = 0
        return max(maxlen, curlen)
