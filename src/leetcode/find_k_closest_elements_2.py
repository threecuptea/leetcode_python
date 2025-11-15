from typing import List
class Solution:
    #####
    # 658. Find K Closest Elements
    # https://leetcode.com/problems/find-k-closest-elements/description/
    #####
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Inspired by neetcode's https://www.youtube.com/watch?v=o-YDQzHoaKM
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            mid = l + (r -l) // 2
            # Compare the outside right element and mid to see if move to right will get closer
            if arr[mid + k] - x < x - arr[mid]:
                l = mid + 1
            else:
                r = mid

        return arr[l:(l + k)]