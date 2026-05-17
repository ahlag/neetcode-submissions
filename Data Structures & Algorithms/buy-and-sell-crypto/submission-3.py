import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        max_diff = 0
        while r < len(prices):
            cur_diff = prices[r] - prices[l]
            if cur_diff >= 0:
                r += 1
                max_diff = max(max_diff, cur_diff)
                continue
            else:
                l += 1
                r = l + 1

        return max_diff

