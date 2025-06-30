class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        minheap = [[0, 0, 0]]
        visit = set()
        directions = [[0,1],
                      [0,-1],
                      [1,0],
                      [-1,0]]
        while minheap:
            diff, r, c = heapq.heappop(minheap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                if (newr<0 or newc<0 or newr == rows or newc == cols or (newr, newc) in visit):
                    continue
                newdiff = max(abs(heights[r][c] - heights[newr][newc]), diff)
                heapq.heappush(minheap, [newdiff, newr, newc])
        