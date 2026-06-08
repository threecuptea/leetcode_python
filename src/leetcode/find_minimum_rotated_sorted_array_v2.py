
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # https://www.youtube.com/watch?v=H2U24n4bcQQ,
        # This version is much better than v1, no hack and much precise
        # exit when l = r
        #  mid = 3, l = 4, r = 6, mid = 5, r = 5, mid = 4, r = 4, l = r = 4, exit because l < r
        # if we want l = r, not mutual exclusive, l < r
        # 0 1 2 3 4 5 6
        # 4 5 6 7 0 1 2
        while  l < r:
            mid = (l + r) // 2
            # mid = 3, l = mid + 1, l = 4, r = 7, mid = 5, happen to be 0,
            # it is in the right section, it definitively move to the right
            if nums[mid] > nums[r]:
                l = mid + 1
            # Must be in the left section. mid can be the target, we don't want to exclude it
            # Need to move to the left
            else:
                r = mid

        return nums[l]

        # if l = mid + 1 or r = mid - 1. There is a chance that l and r will cross and we want it to stop when
        # it cross then we use while l <= r
        # on the other side, l = mid + 1, r = mid. l and r might not cross each other, we want to exit when
        # l == r.  Therefore, we set while l < r