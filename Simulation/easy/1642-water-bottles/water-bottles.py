class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        remaining = numBottles

        while remaining >= numExchange:
            new = remaining // numExchange
            remaining = (remaining % numExchange) + new
            res += new
        return res
