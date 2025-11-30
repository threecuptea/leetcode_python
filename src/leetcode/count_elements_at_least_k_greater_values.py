from collections import Counter
from typing import List
# I wish that I can keep calm and come up with this efficient solution in competition.  This beat 100% runtime and memory
# Lesson learned: Keep calm and don't get irritated.  I can do it.
class Solution:
    #######
    # 3759. Count Elements With at Least K Greater Values
    # https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/
    #######
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        counter = Counter(nums)
        accum = 0
        for key in sorted(counter.keys(), reverse=True):
            accum += counter[key]
            if accum >= k:
                break
        return len(nums) - accum