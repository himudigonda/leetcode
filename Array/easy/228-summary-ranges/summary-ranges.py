class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        left = 0
        while left < len(nums):
            start = nums[left]
            right = left
            while right + 1 < len(nums) and nums[right + 1] == nums[right] + 1:
                right += 1

            if nums[right] == start:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[right]}")
            left = right + 1
        return res
