from typing import List
class Solution:
    ######
    # 198. House Robber
    # https://leetcode.com/problems/house-robber/description/
    ######
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2, prev = 0, nums[0]
        for i in range(1, n):
            curr = max(nums[i] + prev2, prev)
            prev2, prev = prev, curr
        return prev