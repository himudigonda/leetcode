class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        counts = Counter(nums)
        inversecopunts = defaultdict(int)
        print(counts)
        print(inversecopunts)
        for key, val in counts.items():
            inversecopunts[val] = key
        uniq = defaultdict(int)
        for freq in counts.values():
            uniq[freq] += 1
        print(uniq)
        for k, v in uniq.items():
            if v == 1:
                print("v = 1", k, v)
                return inversecopunts[k]
        return -1
