from typing import List
class Solution:
    #########
    # 88. Merge Sorted Array
    # https://leetcode.com/problems/merge-sorted-array/description/
    #
    ##
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        # nums1 and nums2 can be negatives.  It's easier to remove them for comparison
        del nums1[m:]
        i, j = 0, 0
        # len(nums1) keep growing as we insert nums2 character.  So we need re-calculate len(nums1)
        # instead using initial len which would bloc finish processing.  It works when m > n
        while i < len(nums1) and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
        nums1.extend(nums2[j:])