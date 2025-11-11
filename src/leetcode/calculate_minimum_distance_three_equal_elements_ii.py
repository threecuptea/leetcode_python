from collections import defaultdict
from typing import List
class Solution:
    #####
    # Q2. Minimum Distance Between Three Equal Elements II (Contest 475)
    # https://leetcode.com/contest/weekly-contest-475/problems/minimum-distance-between-three-equal-elements-ii/description/
    # Forget Counter approach.  It is faster to loop once O(n)
    ####
    def minimumDistance(self, nums: List[int]) -> int:
        num_map = defaultdict(list)
        min_dist = 999999  # The maximum length is 10^5.  Use a number > 10^5
        for i, num in enumerate(nums):
            num_map[num].append(i)
            # compute the length at the same time. Instead of calculate them after putting together the full list
            if len(num_map[num]) >= 3:
                n = len(num_map[num])
                # j-i + k-j + k-i == 2k - 2i.  That's 2*(num_map[num][n-1]-num_map[num][n-3]) here
                min_dist = min(min_dist, 2*(num_map[num][n-1]-num_map[num][n-3]))
        if min_dist == 999999:
            return -1
        else:
            return min_dist