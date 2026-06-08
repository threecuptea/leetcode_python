# https://leetcode.com/problems/maximum-product-subarray
from typing import List
class Solution:
    # 3 key points:
    # need curr_min becase it can flip to the maximum because the curr num is negative [3, -2, -2]
    # need to take starting a new array into consideration  [2, 3, -2, 8]
    # Keep previous max as tmp
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res, curr_max, curr_min = nums[0], 1, 1

        for num in nums:
            # can start a new subarry
            tmp = curr_max * num
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(tmp, curr_min * num, num)
            res = max(res, curr_max)

        return res