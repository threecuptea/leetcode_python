from typing import List
class Solution:
    ######
    # 322. Coin Change
    # https://leetcode.com/problems/coin-change/description/
    ######
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]