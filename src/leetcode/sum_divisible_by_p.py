from typing import List
class Solution:
    #######
    # 1590. Make Sum Divisible by P
    # https://leetcode.com/problems/make-sum-divisible-by-p/description/
    #######
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        # No need to remove anything
        if target == 0:
            return 0
        curr_m = 0
        mod_map = {curr_m: -1}
        min_len = 999999
        # [3, 1, 4, 2]
        # {0: -1, 3: 0, 4: 1, 2: 2}
        for i, num in enumerate(nums):
            curr_m = (curr_m + num) % p
            # (3 + 1) % 6 = 4, needed modulo 0  This means that we can achieve our goal by remove back up to index -1.
            # i.e. remove 3, 1
            # (2 - x + 6) % 6 = 4. We need to module 4 to make it divisible by 6. x = (2 - 4 + 6) % 6
            # (4 + 4) % 6 = 2 (2 - 4 + 6) % 6 = 4, Need modulo 4 and find index 1. It can remove back up to index 1.
            # i.e. remove 4 alone
            needed = (curr_m - target + p) % p
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
            mod_map[curr_m] = i
            # we cannot remove all elements
        return -1 if min_len == 999999 or min_len  == len(nums) else min_len