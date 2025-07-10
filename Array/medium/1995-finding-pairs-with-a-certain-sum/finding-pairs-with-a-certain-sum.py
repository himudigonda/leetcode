class FindSumPairs:
    # BruteForce
    def __init__(self, nums1: List[int], nums2: List[int]):
        #     self.nums1 = nums1
        #     self.nums2 = nums2
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        #     self.nums2[index] += val
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        #     pairs = 0
        #     for nums1 in self.nums1:
        #         for nums2 in self.nums2:
        #             if nums1 + nums2 == tot:
        #                 pairs += 1
        #     return pairs
        pairs = 0
        for num1val in self.nums1:
            pairs += self.freq2[tot - num1val]
        return pairs


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
