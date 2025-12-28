class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or min(candidates) > target:
            return []

        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total >= target:
                return

            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
                prev = candidates[i]
            return

        dfs(0, [], 0)
        return res
