class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def calc(divisor):
            res = [math.ceil(i / divisor) for i in nums]
            print(divisor, res)
            return sum(res)

        res = float("inf")
        while left <= right:
            mid = (left + right) // 2

            op = calc(mid)
            if op <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left
