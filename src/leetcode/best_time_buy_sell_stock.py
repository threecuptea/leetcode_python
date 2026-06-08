from typing import List
class Solution:
    ######
    # 121. Best Time to Buy and Sell Stock
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    ######
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        # similar to brutal force.  However, only one min
        for p in prices:
            if p < min_price:
                min_price = p
            elif p > min_price:
                max_profit = max(max_profit, pr - min_price)
        return max_profit
