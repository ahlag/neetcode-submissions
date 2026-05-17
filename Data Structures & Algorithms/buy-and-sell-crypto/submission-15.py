class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maximum_profit = 0
        for j in range(1, len(prices)):
            maximum_profit = max(maximum_profit, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
                continue
        return maximum_profit
        