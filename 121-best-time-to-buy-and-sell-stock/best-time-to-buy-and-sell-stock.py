class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = float("-inf")

        for dayprice in prices:
            if dayprice < minprice:
                minprice = dayprice
            if maxprofit < dayprice - minprice:
                maxprofit = dayprice - minprice
        return maxprofit if maxprofit != float("inf") else 0
