from typing import List
class Solution:
    ######
    # 322. Coin Change
    # https://leetcode.com/problems/coin-change/description/
    ######
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # coins sort(reverse=True) does not always get best result
        # coins= [186,419,83,408], 6249.  Cannot analyze and figure out why
        # coins.sort(reverse=True),
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    # if dp[i] != float('inf'): break
        return -1 if dp[amount] == float('inf') else dp[amount]