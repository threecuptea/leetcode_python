# https://leetcode.com/problems/number-of-zigzag-arrays-i/description
from itertools import accumulate
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp.reverse()
            result = list(accumulate(dp[:m-1], initial = 0))
            dp = result

        return (sum(dp) % MOD << 1) % MOD