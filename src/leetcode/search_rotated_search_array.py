from typing import List
class Solution:
    #####
    # https://leetcode.com/problems/search-in-rotated-sorted-array/
    # 33. Search in Rotated Sorted Array
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            # # The solution is inspired by Neetcode  https://www.youtube.com/watch?v=U8XENwh8Oy8  It is intuitive
            # 4, 5, 6, 7, 0, 1, 2
            # the left part of the search tree then narrow down to the right side when either of multiple conditions met
            # using the Take mid as the position of 6 as an example.  It includes two part
            # target > mid value or target < l value. the right side using l pointer to compare, no need to include =
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # the right part of the search tree then narrow down to the left when either of multiple conditions met
            # # 6 7 8 0 1 2 3 4 5, mid = 1
            # either target < mid value or target > r val, left side using r pointer to compare, no need to include =
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1