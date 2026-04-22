import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        diff = 0
        while sell < len(prices):
            if prices[sell] - prices[buy] > 0:
                diff = max(prices[sell] - prices[buy], diff)
            else:
                buy = sell
            sell += 1
        return diff

            