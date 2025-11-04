from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # use a counter on the nums and return the most common from the counter
        # counts = Counter(nums)
        # return [i for i,v in counts.most_common(k)]
    
        # # counter Solution but fully verbose
        # counts = Counter(nums)
        # sorted_counts = sorted(counts.items(), key = lambda x:x[1], reverse = True)
        # return [nums for nums, counts in sorted_counts[:k]]

        # heap Solution
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]