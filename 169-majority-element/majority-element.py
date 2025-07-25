class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # Brute Force
        # freq = 0
        # val = 0

        # for i in range(len(nums)):
        #     if val == nums[i]:
        #         freq += 1
        #     else:
        #         if freq > 0:
        #             freq -= 1
        #         else:
        #             freq = 1
        #             val = nums[i]
        # return val

        # Optimal
        result = 0
        count = 0

        for element in nums:
            if count == 0:
                result = element
            count += 1 if element == result else -1
        return result
