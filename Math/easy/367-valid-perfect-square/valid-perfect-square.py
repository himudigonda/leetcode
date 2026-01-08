class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            cur = mid * mid
            if cur == num:
                return True
            elif cur < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
