class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # # BruteForce
        # i = 0
        # res = [-1] * (len(nums) - k + 1)
        # while i < len(nums) - k + 1:
        #     subarr = nums[i : i + k]
        #     asc = True
        #     for j in range(1, k):
        #         if subarr[j] - subarr[j - 1] != 1:
        #             asc = False
        #             break
        #     if asc:
        #         res[i] = subarr[-1]
        #     i += 1
        # return res

        # Optimal
        n = len(nums)
        res = [-1] * (n - k + 1)
        i, j = 0, 0

        while j < n:
            if j > 0 and nums[j] - nums[j - 1] != 1:
                i = j

            while i < j and j - i + 1 > k:
                i += 1

            if j - i + 1 == k:
                res[j - k + 1] = nums[j]
            j += 1

        return res
