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
        maximum = 0
        dp[0] = nums[0]
        # [2,7,9,3,1]
        for i in range(1, n):
            dp[i] = maximum + nums[i] # dp[2] = 1
            # There is a delay effect because robber cannot rob adjacent house,
            # add dp[0] before we process dp[2], dp[1] is not available for dp[2] yet
            maximum = max(maximum, dp[i - 1])
        # we did not calculate the maximum
        return max(maximum, dp[n - 1])