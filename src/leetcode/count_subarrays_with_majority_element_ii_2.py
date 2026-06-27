# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/description
from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = n # represent 0, [-n, -n-1,....0,...., n-1, n] total 2 * n + 1
        freq = [0] * (2 * n + 1)
        freq[n] = 1 # 0
        less, ans = 0, 0
        for num in nums:
            if num == target:
                less += freq[pref]
                pref += 1
            else:
                pref -= 1
                less -= freq[pref]

            freq[pref] += 1
            ans += less

        return ans