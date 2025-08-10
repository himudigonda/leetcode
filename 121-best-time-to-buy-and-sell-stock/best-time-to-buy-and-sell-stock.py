class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = prices[0]

        for idx, val in enumerate(prices):
            price = val - min_price
            if val < min_price:
                min_price = val
            elif price > max_profit:
                max_profit = price
        return max_profit
