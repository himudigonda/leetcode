class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # HashMap
        # counts = Counter(nums)
        # res = []
        # freq = [[] for i in range(len(nums) + 1)]
        # for key, count in counts.items():
        #     freq[count].append(key)
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        # # Heap
        counts = Counter(nums)
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [keyval[1] for keyval in heap]
