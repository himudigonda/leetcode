class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k -> eating speed -> we decide
        left = 1
        right = max(piles)

        def count_hours(speed):
            res = 0
            for pile in piles:
                res += math.ceil(pile / speed)
            return res

        best = right
        while left <= right:
            mid = (left + right) // 2
            if count_hours(mid) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
