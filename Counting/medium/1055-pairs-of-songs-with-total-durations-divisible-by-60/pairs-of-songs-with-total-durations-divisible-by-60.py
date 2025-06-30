class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] = time[i]%60
        counts = Counter(time)
        print(counts)
        res = 0
        # for i in time:
        #     if 60-i in counts.keys() and counts[60-i]:
        #         counts[60-i] -= 1
        #         res += 1
        #         print(i, 60-i, counts)
        # return res
            
        for i in range(1, 30):
            res += counts[i] * counts[60 - i]
        res += (counts[0] * (counts[0] - 1)) // 2
        res += (counts[30] * (counts[30] - 1)) // 2
        return res