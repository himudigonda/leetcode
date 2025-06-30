class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # # # Sorting and Manipulation
        # # (Number, Index) Pair
        # numsWithIndices = [(num, i) for i, num in enumerate(nums)]

        # # Sort Asc wrt num -val
        # numsWithIndices.sort(key=lambda x: -x[0])

        # # sort Asc wrt index val until top K
        # topK = sorted(numsWithIndices[:k], key=lambda x: x[1])

        # return [num for num, _ in topK]

        # # # Heaps
        arr = []
        heapq.heapify(arr)
        for i in range(len(nums)):
            heapq.heappush(arr, [nums[i], i])
            if len(arr) > k:
                heapq.heappop(arr)
        arr = sorted(arr, key=lambda d: d[1])
        ans = []
        for i in range(len(arr)):
            ans.append(arr[i][0])
        return ans
