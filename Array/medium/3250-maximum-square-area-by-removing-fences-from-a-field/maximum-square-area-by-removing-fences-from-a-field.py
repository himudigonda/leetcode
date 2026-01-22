class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        # h = sorted(hFences + [1, m])
        # v = sorted(vFences + [1, n])

        # sett = set()

        # for i in range(len(h)):
        #     for j in range(i + 1, len(h)):
        #         sett.add(h[j] - h[i])

        # maxarea = -1
        # for i in range(len(v)):
        #     for j in range(i + 1, len(v)):
        #         d = v[j] - v[i]
        #         if d in sett:
        #             maxarea = max(maxarea, d)
        # if maxarea == -1:
        #     return -1
        # return (maxarea**2) % ((10**9) + 7)

        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()

        heights = set()
        widths = set()

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                heights.add(hFences[j] - hFences[i])

        max_side = -1
        widths = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                widths.add(vFences[j] - vFences[i])

        common = heights.intersection(widths)

        if not common:
            return -1

        max_side = max(common)

        return (max_side * max_side) % (10**9 + 7)
