# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 1
        for num in arr[1:]:
            if num - prev > 1:
                curr = prev + 1
            else:
                curr = num
            prev = curr

        return prev