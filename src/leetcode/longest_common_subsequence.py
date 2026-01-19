from functools import cache
class Solution:
    # https://www.youtube.com/watch?v=MNykgz1_ONQ, Greg's
    # https://leetcode.com/problems/longest-common-subsequence/
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # The top-down and memorize approach.
        # text1 = gators
        # text2 = agars
        # If g != a, move the top index and keep the bottom index or move the bottom index and keep the top index
        # otherwise, +1 len to the successful step and move both index.  However, it does require @cache to achieve m * n
        m, n = len(text1), len(text2)
        @cache
        def longest(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                # move both cursor if characters match
                return 1 + longest(i + 1, j + 1)
            else:
                return max(longest(i + 1, j), longest(i, j + 1))

        return longest(0, 0)