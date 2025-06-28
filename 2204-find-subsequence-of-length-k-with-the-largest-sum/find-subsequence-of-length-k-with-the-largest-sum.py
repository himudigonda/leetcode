class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # (Number, Index) Pair
        numsWithIndices = [(num, i) for i, num in enumerate(nums)]

        # Sort Asc wrt num -val
        numsWithIndices.sort(key=lambda x: -x[0])

        # sort Asc wrt index val until top K
        topK = sorted(numsWithIndices[:k], key=lambda x: x[1])

        return [num for num, _ in topK]
