class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistanceToOrigin(x, y):
            return math.sqrt((x * x) + (y * y))

        heap = []
        heapq.heapify(heap)
        for x, y in points:
            dist = calcDistanceToOrigin(x, y)
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
