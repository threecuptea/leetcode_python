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
            else:
                profit = p - min_price
                if profit > 0:
                    max_profit = max(max_profit, profit)
        return max_profit
