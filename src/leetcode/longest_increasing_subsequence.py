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
        # max count to include
        # idx.         0,  1,  2
        #              1,  3,   6,   9,   4,  10, 5, 6
        # count        1.  2.   3.   4,   3,   5
        for i in range(1, n):
            # num[i] compares with any index before 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # if nums[i] cannot anything smaller, it would remain 1
        return max(dp)
