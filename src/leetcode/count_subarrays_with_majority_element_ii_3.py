# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/description
from typing import List
from collections import defaultdict
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = 0
        freq = defaultdict(int)
        freq[0] = 1
        less, ans = 0, 0
        # [1,2,2,3], pref: [0, -1, 0, 1, 0], freq = {0: 1} to start
        for num in nums:
            if num == target:
                # when curr(prefix) = 1, I can include freq[0] in less, don't forget less is an accumulated number less = 1 + 2, (freq[-1] + freq[0] )
                less += freq[pref]
                pref += 1
            else:
                # less was calculated using curr = 1 after the 2nd 2, when num = 3, curr (prefix)= 0, freq[0] can no longer be applied in less
                pref -= 1
                less -= freq[pref]

            freq[pref] += 1 # {0: 1, -1, 0} -> {-1: 1, 0: 2, 1:1}
            ans += less

        return ans