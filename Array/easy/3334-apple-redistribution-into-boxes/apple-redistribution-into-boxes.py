class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity = sorted(capacity, reverse=True)
        total = sum(apple)
        res = 0
        i = 0
        while total > 0:
            res += 1
            total -= capacity[i]
            i += 1
        return res
