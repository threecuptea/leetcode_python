# https://leetcode.com/problems/maximum-total-subarray-value-i/
from typing import List
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        idx_num = []
        n = len(nums)
        for idx, num in enumerate(nums):
            idx_num.append((num, idx))
        # 5, 4, 2, 1
        s_nums = sorted(idx_num, key= lambda pair: -(pair[0]))

        l, r = 0, n - 1
        rem, summ = k, 0
        while True:
            # num diff
            diff = s_nums[l][0] - s_nums[r][0]
            # compare idx, idx diff
            avail = min(n - abs(s_nums[l][1] - s_nums[r][1]), rem)
            summ += avail *  diff
            rem -= avail
            if rem == 0:
                break
            if l - r <= 1:
                break
            if (s_nums[l + 1][0] - s_nums[r][0]) >= (s_nums[l][0] - s_nums[r - 1][0]):
                l += 1
            else:
                r -= 1
        if rem > 0:
            summ += (s_nums[l][0] - s_nums[r][0]) * rem
        return summ
