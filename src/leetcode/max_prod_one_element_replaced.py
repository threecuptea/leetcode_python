
from typing import List
class Solution:
    #####
    # Q2. Maximum Product of Three Elements After One Replacement©leetcode
    # https://leetcode.com/contest/weekly-contest-474/problems/maximum-product-of-three-elements-after-one-replacement/description/
    ####
    def maxProduct(self, nums: List[int]) -> int:
        st = sorted(nums)
        prod_f = st[0] * st[1]
        prod_b = st[len(st)-1] * st[len(st)-2]
        # I thought the prod of the first two or the last two will produce the larget prod.
        # It covers most of cases.  However, 0 can be in the middle.  The prod of the 1st and the last produce the maximum.
        prod_c = st[0] * st[len(st)-1]
        m = max(abs(prod_f), abs(prod_b), abs(prod_c))
        return m * 100000