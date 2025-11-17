from typing import List
class Solution:
    ######
    # 300. Longest Increasing Subsequence
    # https://leetcode.com/problems/longest-increasing-subsequence/description/
    # ######
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        dp[0] = 1
        # index-0 base
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
