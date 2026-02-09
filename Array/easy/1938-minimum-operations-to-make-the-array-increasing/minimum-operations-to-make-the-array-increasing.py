class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]

        for idx in range(1, len(nums)):
            if prev >= nums[idx]:
                temp = prev - nums[idx] + 1
                count += temp
                prev += 1
            else:
                prev = nums[idx]
        return count

        # res = 0
        # prev = nums[0]

        # for num in nums[1:]:
        #     if prev < num:
        #         prev = num
        #         continue

        #     res += prev + 1 - num
        #     prev = prev + 1
        # return res
