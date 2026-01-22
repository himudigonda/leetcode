class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # n = len(nums)
        # prefix = [0] * n
        # suffix = [0] * n

        # for i in range(1, n):
        #     prefix[i] = nums[i - 1] + prefix[i - 1]

        # for i in range(n - 2, -1, -1):
        #     suffix[i] = nums[i + 1] + suffix[i + 1]

        # for i in range(n):
        #     if prefix[i] == suffix[i]:
        #         return i
        # return -1

        left = 0
        right = sum(nums)

        for idx, num in enumerate(nums):
            right -= num
            if right == left:
                return idx
            left += num
        return -1
