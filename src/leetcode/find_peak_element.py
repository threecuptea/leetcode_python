from typing import List
class Solution:
    #####
    # 162. Find Peak Element
    # https://leetcode.com/problems/find-peak-element/description/
    #####
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # Do I need to consider l = r, n = 1 case, yes, need to be equal
        while l <= r:
            mid = l + (r-l) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                r = mid - 1
            elif mid < len(nums)-1 and nums[mid+1] > nums[mid]:
                l = mid + 1
            # This cover 3 cases: mid is not at two end,  and it is greater than its closest right and left neighbor
            # That is the most common one and the right end & its left neighbor is not greater than it
            # or the left end and its right neighbor is great than it
            else:
                return mid