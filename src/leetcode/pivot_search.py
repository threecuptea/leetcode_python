# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/search-timestamp-in-rotated-log-timestamps/problem
# It's the same as https://leetcode.com/problems/search-in-rotated-sorted-array/
def searchRotatedTimestamps(nums, target):
    # Write your code here
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + ((r -l) // 2)
        if nums[mid] == target:
            return mid
        # 4 5 6 7 8 0 1 2 3
        if nums[mid] >= nums[l]:
            # under what condition, it would be on the right side, mid= 7,
            # either 8 or 0 1 2 3
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # 6 7 8 0 1 2 3 4 5, mid = 1
        else:
            if target < nums[mid] or target > nums[r]:
                r =  mid - 1
            else:
                l = mid + 1
    return -1