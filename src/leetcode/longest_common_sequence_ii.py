class Solution:
    # https://www.youtube.com/watch?v=MNykgz1_ONQ, Greg's
    # https://leetcode.com/problems/longest-common-subsequence/
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # will have dp matrix
        m, n = len(text1), len(text2)
        dp = []
        for _ in range(m + 1):
            dp.append([0] * (n + 1))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]