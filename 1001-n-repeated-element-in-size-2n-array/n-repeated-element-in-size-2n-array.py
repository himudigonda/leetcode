import random

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        while True:
            a, b = random.sample(range(len(nums)), 2)
            if nums[a] == nums[b]:
                return nums[a]