class Solution:
    def reorganizeString(self, s: str) -> str:
        # # BruteForce
        # count = Counter(s)
        # maxHeap = [[-cnt, char] for char, cnt in count.items()]
        # heapq.heapify(maxHeap)

        # prevMax = None
        # res = ""
        # while maxHeap or prevMax:
        #     if prevMax and not maxHeap:
        #         return ""
        #     cnt, char = heapq.heappop(maxHeap)
        #     res += char
        #     cnt += 1
        #     if prevMax:
        #         heapq.heappush(maxHeap, prevMax)
        #         prevMax = None
        #     if cnt != 0:
        #         prevMax = [cnt, char]
        # return res

        # Optimal
        count = Counter(s)
        maxHeap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prevMax, prevCount = "", 0
        res = []

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res.append(char)
            if prevCount < 0:
                heapq.heappush(maxHeap, (prevCount, prevMax))
            prevCount, prevMax = count + 1, char

        res = "".join(res)

        return res if len(res) == len(s) else ""
