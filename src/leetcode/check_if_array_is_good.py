# https://leetcode.com/problems/check-if-array-is-good/description/
from collections import Counter
from typing import List
def isGood(self, nums: List[int]) -> bool:
    n = max(nums)
    if len(nums) != n + 1:
        return False
    if min(nums) != 1:
        return False

    counter = Counter(nums)
    if counter[n] != 2:
        return False
    for i in range(1, n):
        if counter.get(i) != 1:
            return False
    return True