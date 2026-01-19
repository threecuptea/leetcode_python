
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # we only have one number, 10, the target = 10, l = r = 0,
        # it won't even execute while loop if l < r.
        # It's different from threesum case where l, r represents unique index of array to sum up
        while l <= r:
            m = l + ((r -l) // 2)
            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1