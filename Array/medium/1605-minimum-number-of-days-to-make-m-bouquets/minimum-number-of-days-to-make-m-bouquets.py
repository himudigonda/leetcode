class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def checkifgood(day):
            counter = 0
            res = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    counter += 1
                else:
                    res += counter // k
                    counter = 0
            res += counter // k
            return res >= m

        right = max(bloomDay)
        left = min(bloomDay)

        best = -1
        while left <= right:
            print(best)
            mid = (left + right) // 2
            if checkifgood(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
