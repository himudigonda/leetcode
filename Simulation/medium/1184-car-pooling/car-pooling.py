class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minheap = []
        curpass = 0
        for t in trips:
            numpass, start, end = t
            while minheap and minheap[0][0] <= start:
                curpass -= minheap[0][1]
                heapq.heappop(minheap)

            curpass += numpass
            if curpass > capacity:
                return False
            heapq.heappush(minheap, [end, numpass])
        return True
