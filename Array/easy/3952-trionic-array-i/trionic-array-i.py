class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        peak = -1
        valley = -1

        for i in range(n - 1):
            if peak == -1 and nums[i] >= nums[i + 1]:
                peak = i

            j = n - 1 - i
            if valley == -1 and nums[j] <= nums[j - 1]:
                valley = j

        if peak <= 0 or valley >= n - 1 or peak >= valley:
            return False

        for k in range(peak, valley):
            if nums[k] <= nums[k + 1]:
                return False
        return True
