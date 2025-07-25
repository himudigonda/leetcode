class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # Brute Force
        # total = 0
        # maxtotal = 0
        # for num in nums:
        #     if total < 0:
        #         total = 0
        #     total += num
        #     maxtotal = max(maxtotal, total)
        # return maxtotal

        # Optimal
        total = nums[0]
        maxtotal = nums[0]
        for num in nums[1:]:
            total = max(total + num, num)
            maxtotal = max(maxtotal, total)
        return maxtotal
