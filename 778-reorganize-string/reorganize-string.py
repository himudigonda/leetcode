class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prevMax = None
        res = ""
        while maxHeap or prevMax:
            if prevMax and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            if prevMax:
                heapq.heappush(maxHeap, prevMax)
                prevMax = None
            if cnt != 0:
                prevMax = [cnt, char]
        return res
