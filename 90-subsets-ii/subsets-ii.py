class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(idx, curarr):
            if idx > len(nums):
                return
            res.append(curarr.copy())

            prev = None
            for i in range(idx, len(nums)):
                if nums[i] == prev:
                    continue
                curarr.append(nums[i])
                dfs(i + 1, curarr)
                curarr.pop()
                prev = nums[i]
            return

        dfs(0, [])
        return res
