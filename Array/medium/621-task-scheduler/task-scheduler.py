class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        time = 0
        heap = []
        q = deque()
        heapq.heapify(heap)
        for count in Counter(tasks).values():
            heapq.heappush(heap, -count)

        while heap or q:
            time += 1

            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
