class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        left = 0
        right = x // 2
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x:
                right = mid - 1
            elif mid**2 <= x:
                best = mid
                left = mid + 1
            # else:
            #     best = mid
            #     break
        # return best
        return right
