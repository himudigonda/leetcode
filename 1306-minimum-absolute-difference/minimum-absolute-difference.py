class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1,2,3,4

        arr.sort()
        min_diff = float("inf")
        res = []
        for idx in range(1, len(arr)):
            diff = arr[idx - 1] - arr[idx]
            print(diff, arr[idx - 1], arr[idx])
            if abs(diff) < abs(min_diff):
                min_diff = diff
                res = [[arr[idx - 1], arr[idx]]]
            elif abs(diff) == abs(min_diff):
                res.append([arr[idx - 1], arr[idx]])
        return res
