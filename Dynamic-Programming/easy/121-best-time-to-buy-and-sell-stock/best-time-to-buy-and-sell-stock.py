class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxprofit = 0
        minprice = prices[0]

        for idx, val in enumerate(prices):
            if val < minprice:
                minprice = val
            elif val - minprice > maxprofit:
                maxprofit = val - minprice

        return maxprofit
