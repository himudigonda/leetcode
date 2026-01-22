class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        side = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                minx = max(bottomLeft[i][0], bottomLeft[j][0])
                maxx = min(topRight[i][0], topRight[j][0])
                miny = max(bottomLeft[i][1], bottomLeft[j][1])
                maxy = min(topRight[i][1], topRight[j][1])

                if minx < maxx and miny < maxy:
                    length = min(maxx - minx, maxy - miny)
                    side = max(side, length)
        return side**2
