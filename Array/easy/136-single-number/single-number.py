class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # mapping = Counter(nums)
        # return sorted(mapping.items(), key=lambda x: x[1])[0][0]

        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        return sorted(mapping.items(), key=lambda x: x[1])[0][0]
