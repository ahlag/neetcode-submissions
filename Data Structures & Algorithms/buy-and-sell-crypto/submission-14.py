class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maximum_profit = 0
        for j in range(1, len(prices)):
            if prices[j] < prices[i]:
                i = j
                continue
            maximum_profit = max(maximum_profit, prices[j] - prices[i])

            
        return maximum_profit
        