class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # # Bruteforce
        # count = 0
        # left = 0

        # for i in range(1, len(nums) - 1):
        #     if nums[i] != nums[i + 1]:
        #         if (nums[i] > nums[left] and nums[i] > nums[i + 1]) or (
        #             nums[i] < nums[left] and nums[i] < nums[i + 1]
        #         ):
        #             count += 1
        #         left = i

        # return count

        # Optimal
        compNum = []
        if not nums:
            return 0

        compNum.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                compNum.append(nums[i])

        count = 0
        if len(compNum) < 3:
            return 0

        for i in range(1, len(compNum) - 1):
            left = compNum[i - 1]
            cur = compNum[i]
            right = compNum[i + 1]
            if (cur > left and cur > right) or (cur < left and cur < right):
                count += 1
        return count
