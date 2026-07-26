# https://leetcode.com/problems/maximum-product-of-three-numbers
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            return nums[0] * nums[1] * nums[2]
        pos, neg = [], []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        if pos: pos.sort(reverse = True)
        if neg: neg.sort()
        if pos and not neg:
            return pos[0] * pos[1] * pos[2]
        if not pos and neg:
            return neg[n - 1] * neg[n - 2] * neg[n - 3]
        options = []
        if len(neg) >= 2:
            options.append(neg[0] * neg[1] * pos[0])
        if len(pos) >= 3:
            options.append(pos[0] * pos[1] * pos[2])

        return max(options)