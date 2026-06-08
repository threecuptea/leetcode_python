from typing import List
class Solution:
    # credits to https://www.youtube.com/watch?v=Aivg_MSs2w4
    # https://leetcode.com/problems/house-robber-ii
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # [20, [9, 12, 3], 25], we take 20 plus the maximum([12, 3] using rob_basic
        # we take 25 plus the maximum of ([9, 12]) using rob_basic or
        # we don't take either one and we just the maximum of [9, 12, 3] as rob_basic
        def rob_basic(nums2: List[int]):
            if len(nums2) == 0:
                return 0
            n2 = len(nums2)
            prev2, prev = 0, nums2[0]
            for i in range(1, n2):
                curr = max(nums2[i] + prev2, prev)
                prev2, prev = prev, curr
            return prev

        return max(nums[0] + rob_basic(nums[2:n - 1]), rob_basic(nums[1:n - 2]) + nums[n - 1], rob_basic(nums[1:n - 1]))