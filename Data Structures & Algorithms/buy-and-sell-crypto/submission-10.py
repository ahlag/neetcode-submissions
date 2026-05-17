import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            cur_profit = prices[j] - prices[i]
            if cur_profit >= 0:
                max_profit = max(max_profit, cur_profit)
                j += 1
            else:
                i += 1
                j = i + 1
        
        return max_profit


