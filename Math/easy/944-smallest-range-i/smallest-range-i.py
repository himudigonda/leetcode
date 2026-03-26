class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        minn = min(nums)
        ans = (maxx - k) - (minn + k)

        return ans if ans > 0 else 0
