#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            if target-n in map:
                return [map[target-n], i]
            else:
                map[n] = i
        return []


# @lc code=end
