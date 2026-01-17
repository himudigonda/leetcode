class Solution:
    def bestTower(
        self, towers: List[List[int]], center: List[int], radius: int
    ) -> List[int]:
        # towers.sort(key=lambda x: (-x[2], x[0], x[1]))

        # for x, y, q in towers:
        #     rad = abs(x - center[0]) + abs(y - center[1])
        #     if rad <= radius:
        #         return [x, y]

        # return [-1, -1]

        cx, cy = center
        bestq = -1
        bestx = -1
        besty = -1

        for x, y, q in towers:
            if abs(x - cx) + abs(y - cy) <= radius:
                if q > bestq or (
                    q == bestq and (x < bestx or (x == bestx and y < besty))
                ):
                    bestq = q
                    bestx = x
                    besty = y
        return [bestx, besty]
