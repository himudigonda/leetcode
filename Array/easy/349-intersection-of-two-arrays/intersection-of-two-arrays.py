class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        countA = Counter(nums1)
        countB = Counter(nums2)

        res = []
        for key, val in countA.items():
            if key in countB:
                res.append(key)
        return res
