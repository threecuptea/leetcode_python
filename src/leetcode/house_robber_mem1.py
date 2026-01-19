from typing import List
class Solution:
######
# 198. House Robber
# https://leetcode.com/problems/house-robber/description/
######
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        maximum = 0
        # 2, 1, 1, 2
        # 2, 7, 9, 3, 1
        # 1, 2, 3, 1
        prev, curr = nums[0], 0
        for i in range(1, n):
            curr = maximum + nums[i]
            maximum = max(maximum, prev)
            prev = curr
        return max(maximum, curr)