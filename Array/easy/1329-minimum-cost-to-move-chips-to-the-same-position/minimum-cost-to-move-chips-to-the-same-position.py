class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # res = 0
        # maxcount = float("-inf")
        # maxnum = float("-inf")
        # counts = Counter(position)
        # for idx, count in counts.items():
        #     if count > maxcount:
        #         maxcount = max(maxcount, count)
        #         maxnum = idx

        # for idx, count in counts.items():
        #     res += (abs(idx - maxnum) % 2) * count

        # return res
        evens = [val for val in position if val % 2 == 0]
        odds = [val for val in position if val % 2 == 1]
        return min(len(evens), len(odds))
            