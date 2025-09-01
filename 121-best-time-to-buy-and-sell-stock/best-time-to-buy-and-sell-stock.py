class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = float("-inf")

        for index, val in enumerate(prices):
            if val < min_price:
                min_price = val
            if max_profit < val - min_price:
                max_profit = val - min_price
        return max_profit if max_profit != float("-inf") else 0
