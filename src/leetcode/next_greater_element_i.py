
from typing import List
class Solution:
    ######
    # 496. Next Greater Element I
    # https://leetcode.com/problems/next-greater-element-i/description/
    ######
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answers = [-1] * len(nums1)
        stk = []
        for i, num in enumerate(nums2):
            while stk and num > stk[-1][0]:
                stk_n, stk_i = stk.pop()
                answers[stk_i] = num
            if num in nums1:
                idx = nums1.index(num)  # index in nums1 (2, 0)
                # records (1, 1)
                stk.append((num, idx))
        return answers