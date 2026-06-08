from typing import List
class Solution:
    #####
    # https://leetcode.com/problems/search-in-rotated-sorted-array/
    # 33. Search in Rotated Sorted Array
    def search(self, nums: List[int], target: int) -> int:
        # borrow findMin
        n = len(nums)
        l, r = 0, n - 1
        while  l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        min_idx = l
        # 3 scenario, set l, r accordingly, then use regular binary search
        # 1. no rotated or fully rotated array
        if min_idx == 0:
            l, r = 0, n - 1
        # 2. the right partition
        elif nums[0] <= target <= nums[min_idx - 1]:
            l, r = 0, min_idx - 1
        # 3. the left partition
        else:
            l, r = min_idx, n - 1
        while  l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1