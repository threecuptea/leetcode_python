import math
class Solution:
    #  https://leetcode.com/problems/unique-paths/
    def uniquePaths(self, m: int, n: int) -> int:

        # 7 * 3.  Will choose two columns to go down 8 choose 2, the rest of column will go right
        # return math.comb(m + n - 2, m - 1)
        #  1  1  1  1  1   1  1
        #  1. 2  3  4  5   6  7
        #. 1  3  6  10 15 21 28
        dp = []
        # how to in itialize multi-dimensional array
        for i in range(m):
            dp.append([0] * n)
        dp [0][0] = 1  # one way to get there

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = 0
                if i > 0:
                    val += dp[i - 1][j]
                if j > 0:
                    val += dp[i][j - 1]
                dp[i][j] = val

        return dp[m - 1][n - 1]