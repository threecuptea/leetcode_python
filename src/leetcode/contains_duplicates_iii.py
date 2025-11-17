
from sortedcontainers import SortedList
from typing import List
class Solution:
    #####
    #220. Contains Duplicate III
    # https://leetcode.com/problems/contains-duplicate-iii/description/
    #####
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        sd = SortedList()
        for i, num in enumerate(nums):
            if i == 0:
                sd.add(num)
            else:
                low = num - valueDiff
                ip = sd.bisect_left(low)
                if ip < len(sd):
                    if sd[ip] <= num + valueDiff:
                        return True
                if len(sd) == indexDiff:
                    num_to_r = nums[i - indexDiff]
                    ip = sd.bisect_left(num_to_r)
                    del sd[ip]
                sd.add(num)
        return False
