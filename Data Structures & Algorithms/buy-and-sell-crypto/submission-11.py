import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit >= 0:
                max_profit = max(max_profit, profit)
            else:
                i += 1
                j = i
            j += 1
        return max_profit


