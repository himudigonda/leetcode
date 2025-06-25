class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        # freq = defaultdict(list)

        for key, count in counts.items():
            freq[count].append(key)

        # while len(res)<k:
        #     res.append(freq[-1])
        #     freq.pop()
        # return res
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
