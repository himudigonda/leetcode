class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = defaultdict(int)
        suffix = Counter(nums)
        res = []

        for i in nums:
            prefix[i] += 1
            suffix[i] -= 1
            if suffix[i] == 0:
                del suffix[i]
            res.append(len(prefix) - len(suffix))
        return res
