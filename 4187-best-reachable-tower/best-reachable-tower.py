class Solution:
    def bestTower(
        self, towers: List[List[int]], center: List[int], radius: int
    ) -> List[int]:
        towers.sort(key=lambda x: (-x[2], x[0], x[1]))

        for x, y, q in towers:
            rad = abs(x - center[0]) + abs(y - center[1])
            if rad <= radius:
                return [x, y]

        return [-1, -1]
