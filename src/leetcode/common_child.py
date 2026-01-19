# https://www.hackerrank.com/challenges/common-child/problem
# https://leetcode.com/problems/longest-common-subsequence/
# https://www.youtube.com/watch?v=MNykgz1_ONQ
def commonChild(s1, s2):
    # Write your code here
    m, n = len(s1), len(s2)
    dp = []
    for _ in range(m + 1):
        dp.append([0] * (n + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j -1]:
                dp[i][j] = dp[i - 1][j -1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]