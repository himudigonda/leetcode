class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        target = start ^ goal
        count = 0
        while target > 0:
            count += target & 1
            target = target >> 1
        return count
