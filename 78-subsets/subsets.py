class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur, i):
            if i == len(nums):
                res.append(cur[:])
                return

            cur.append(nums[i])
            backtrack(cur, i + 1)

            cur.pop()
            backtrack(cur, i + 1)

        backtrack([], 0)
        return res
