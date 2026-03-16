class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        counts = Counter(nums)
        inversecopunts = defaultdict(int)
        for key, val in counts.items():
            inversecopunts[val] = key
        uniq = defaultdict(int)
        for freq in counts.values():
            uniq[freq] += 1
        for k, v in uniq.items():
            if v == 1:
                return inversecopunts[k]
        return -1
