import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        max_in_piles = max(piles)

        def count_hours(speed):
            res = 0
            for pile in piles:
                res += math.ceil(pile / speed)
            return res
        
        min_eating_speed = 1
        max_eating_speed = max_in_piles
        best = max_in_piles
        while min_eating_speed <= max_eating_speed:
            speed = (min_eating_speed + max_eating_speed) // 2
            hours_to_eat_all = count_hours(speed)
            if hours_to_eat_all <= h:
                best = min(speed, best)
                max_eating_speed = speed - 1
            else:
                min_eating_speed = speed + 1
        return best