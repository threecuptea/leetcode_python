
from typing import List
class Solution:
####
#  153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
####
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        # Do I need to consider l = r, n = 1 case, yes, need to be equal.  No need to think about which
        while l <= r:
            # There are two keep rising slopes parts.  One of them has the minimum point. They have common threads
            # as the following
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = l + (r -l) // 2
            result = min(result, nums[mid])  # in case mid happen to be the lowest point and got lost when move right or left
            # need to include equal since the the very beginning can be the answer
            # In the left section, [4,5,6,7,0,1,2], [11, 13, 15, 17]
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result