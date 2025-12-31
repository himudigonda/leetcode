class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        cur = 1
        res = []
        for cur in range(1, len(mountain) - 1):
            if mountain[cur - 1] < mountain[cur] > mountain[cur + 1]:
                res.append(cur)
        return res
