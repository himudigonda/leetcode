class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        heap = []
        for idx, sc in enumerate(score):
            heapq.heappush(heap, (-sc, idx))

        rank = [0] * n

        place = 1
        while heap:
            og_idx = heapq.heappop(heap)[1]
            if place == 1:
                rank[og_idx] = "Gold Medal"
            elif place == 2:
                rank[og_idx] = "Silver Medal"
            elif place == 3:
                rank[og_idx] = "Bronze Medal"
            else:
                rank[og_idx] = str(place)
            place += 1

        return rank
