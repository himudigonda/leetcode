from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # simple return by comapring lens of input and set version of input
        # return len(nums) != len(set(nums))
        
        # next is to do the same while iterating and 
        # adding each into the set to see if dups exist
        sett = set()
        for i in nums:
            if i in sett:
                return True
            sett.add(i)
        return False

        # # next is to sort it and compare adj elements.
        # # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]: return True
        # return False

        # # next method is to use freq maps
        # counts = defaultdict()
        # for i in nums:
        #     if counts.get(i) == 1: return True
        #     else: counts[i] = 1
        # return False

        # # BruteForce
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]: return True
        # return False