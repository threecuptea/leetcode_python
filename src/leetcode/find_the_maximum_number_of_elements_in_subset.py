# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description
from collections import Counter
from math import isqrt
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 2**4 = 65536, 2**5 = 4294967296 > 10**9, in another word, other than 1,
        # the max length of array [2, 4, 16, 256, 65536, 256, 16, 4, 2] == 9, p ==4
        # [4, 16, 256, 65536, 256, 16, 4]
        # [14, 196, 38416, 196, 14]
        # [178, 31684, 178]
        # [31623]
        # d = {9: 4, 7: 14, 5: 178, 3:31623, 1: 10**9} # sqrt(10**9) upper bound, sqrt(31622) upper bound, 178, 14
        cnt = Counter(nums)
        one_cnt = cnt[1]
        ans = 0
        if one_cnt > 0:
            ans = one_cnt if one_cnt % 2 else one_cnt - 1 # need odd number
        cnt.pop(1, None)
        for num in cnt:
            x = num
            sq = isqrt(x)
            if sq * sq == x and cnt[sq] > 1:
                # num. can be sqrt, get the smallest
                continue
            n = 0
            # 31663 * 31633 > 10**9
            while x <= 31622 and cnt[x] > 1:
                # Only the peak one has 1, the rest has at least 2
                n += 2
                x *= x
            ans = max(ans, n + (1 if x in cnt else -1)) # if the peak exists, n + 1 else drop the next smaller one, drop n

        return ans