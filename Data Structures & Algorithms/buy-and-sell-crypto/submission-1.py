class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            max_profit = max(max_profit, prices[i] - lowest)
        return max_profit