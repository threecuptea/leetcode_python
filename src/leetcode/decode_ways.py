
# https://leetcode.com/problems/decode-ways
class Solution:
    # https://www.youtube.com/watch?v=g1nFbi7bIV0, Credit to Deepti Talesra's video
    # Consider this as a Fbonacci or Climb Stairs with conditional twist.
    # They both combine results of previous two DPs: the previous one for single-digit sequences and the previous 2nd
    # for double-digit sequences
    # The latter will only add when two-digit represents 10 <= nums <= 26. For '0' it can only be matched in two-digit way.
    # The combined with the previous one got to be '10' or '20'. If it fails, all following DP will be 0 and the final
    # result will be 0 too.  That's the brilliant part.
    # For example, '1123'.  1 for the initial 1 composition of no initial character as a placeholder.
    # the first 1 inherit 1 and no two-digit combination dp[1] = 1
    # the second 1 inherit 1 for single digit represent (1, 1), then check double-digit 11 falling in the range, taking
    # number from no initial sequence, represents (11) dp[2] = 2
    # move to '2' inherits for single-digit from dp[2]: [(1, 1, 2), (11, 2)], then check double-digit 11 falling in the range
    # how many numbers of initial sequences can it be: 1 for the first 1, get it from dp[1], represents (1, 12), dp[3] = 2 + 1 = 3
    # move to '3', take dp[3] for single-digit, represents [(1, 1, 2, 3), (11, 2, 3), (1, 12, 3).
    # then check double-digit 23 falling in the range. How many numbers of initial sequences can it be '11'?
    # It's 2; getting it from dp[2], represents [(1, 1, 23), (11, 23)], dp[4] = 5
    # The sequence: 1 1 2 3 5 seems familiar? That's Fbonacci sequences.  However, it has constraints. If the example is
    # '11234'. It will only inherit dp[4] for single-digit and won't inherit dp[3] for double-digit because 34 does not
    #  fall in the range.  The count sequence will be 1 1 2 3 5 5
    # '0' will reset the sequence. For example, '1120'. Even though dp[3] = 3, we won't be able to use those sequences
    # because we need to pull 2 in to combine as 20.  Therefore, we can only count on those sequence up the second '1': dp[2]
    # dp[4] = dp[2] = 2.  That's the  final result. It represents [(1, 1, 20), (11, 20)]
    # For example, the final result for '3802' is 0. dp[2] = 2, '0' does not match single-digit wise, '80' does not match
    # double-digit wise, dp[3] = 0, dp[4] inherit 0 from dp[3] and '02' does not match double-digit wise: dp[4] = 0. Since
    # the previous 2 dp are 0, dp will be 0 all the way even for the example is like '38026123'.
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        # 2, 2, 6
        dp = [1, 1]
        for idx, num in enumerate(s[1:], 2):
            ways = 0
            if num != '0':
                ways += dp[idx - 1]
            # idx = 2, num = 2
            if 10 <= int(s[idx - 2: idx]) <= 26:
                ways += dp[idx - 2]
            dp.append(ways)
        return dp[-1]