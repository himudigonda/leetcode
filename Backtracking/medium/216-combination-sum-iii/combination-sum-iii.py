class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        res = []

        def dfs(idx, cursum, curnums):
            if idx > len(nums) or cursum > n:
                return
            if cursum == n and len(curnums) == k:
                res.append(curnums.copy())
            for i in range(idx, len(nums)):
                curnums.append(nums[i])
                dfs(i + 1, cursum + nums[i], curnums)
                curnums.pop()
            return

        dfs(0, 0, [])
        return res
