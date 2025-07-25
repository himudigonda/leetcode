class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 0
        val = 0

        for i in range(len(nums)):
            if val == nums[i]:
                freq += 1
            else:
                if freq > 0:
                    freq -= 1
                else:
                    freq = 1
                    val = nums[i]
        return val
