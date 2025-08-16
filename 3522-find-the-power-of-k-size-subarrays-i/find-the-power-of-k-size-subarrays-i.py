class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # BruteForce
        i = 0
        res = [-1] * (len(nums) - k + 1)
        while i < len(nums) - k + 1:
            subarr = nums[i : i + k]
            asc = True
            for j in range(1, k):
                if subarr[j] - subarr[j - 1] != 1:
                    asc = False
                    break
            if asc:
                res[i] = subarr[-1]
            i += 1
        return res
