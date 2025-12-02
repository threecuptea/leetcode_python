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
        # max = max(rob_next, rob_next_plus_1 + nums[i])
        rob_next_plus_1 = 0 # nums[n], no house left to rob
        rob_next = nums[n-1]
        # At least one loop, n >= 2
        for i in range(n-2, -1, -1):
            curr = max(rob_next, rob_next_plus_1 + nums[i])
            rob_next_plus_1 = rob_next
            rob_next = curr
        return curr