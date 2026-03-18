class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or min(candidates) > target:
            return []
        res = []

        def findSum(idx, cursum, curcand):
            if cursum == target:
                res.append(curcand.copy())
                return
            if idx >= len(candidates) or cursum > target:
                return

            curcand.append(candidates[idx])
            # cursum += candidates[idx]
            # findSum(idx, cursum, curcand)
            findSum(idx, cursum + candidates[idx], curcand)

            curcand.pop()
            # cursum -= candidates[idx]
            findSum(idx + 1, cursum, curcand)
            return

        findSum(0, 0, [])
        return res
