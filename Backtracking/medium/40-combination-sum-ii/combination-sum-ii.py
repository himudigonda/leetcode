class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or min(candidates) > target:
            return []

        res = list()
        candidates.sort()

        def findsum(idx, cursum, curcand):
            if cursum == target:
                res.append(curcand.copy())
                return
            if idx >= len(candidates) or cursum > target:
                return

            prev = -1
            for i in range(idx, len(candidates)):
                if cursum + candidates[i] > target:
                    break
                if candidates[i] == prev:
                    continue
                curcand.append(candidates[i])
                findsum(i + 1, cursum + candidates[i], curcand)
                curcand.pop()
                prev = candidates[i]
            return

        findsum(0, 0, [])
        return res
