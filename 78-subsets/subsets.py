class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):
            subsets = []
            for j in range(n):
                if i & (1 << j):
                    subsets.append(nums[j])
            res.append(subsets)
        return res
