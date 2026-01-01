class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = float("-inf")
        minprice = float("inf")

        for price in prices:
            # if price < minprice:
            #     minprice = price
            # if price - minprice > maxprofit:
            #     maxprofit = price - minprice
            
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit
