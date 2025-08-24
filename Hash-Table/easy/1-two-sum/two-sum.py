class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Optimal Solution
        hashset = {}
        n = len(nums)

        for i in range(n):
            to_find = target - nums[i]
            if to_find in hashset:
                return [i, hashset[to_find]]
            else:
                hashset[nums[i]] = i
        return []
