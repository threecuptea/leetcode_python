from typing import List
class Solution:
    ######
    # 198. House Robber
    # https://leetcode.com/problems/house-robber/description/
    ######
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # 2, 1, 1, 2
        for i in range(2, n):
            # dp[1] has already taken max(dp[0], dp[1] into consideration. It chose not to take nums[1]
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp[n-1], dp[n-2])

