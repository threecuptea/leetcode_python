# https://neetcode.io/problems/permutation-string
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        l = 0
        counter_s1 = Counter(s1)
        while l <= n2 - n1:
            if s2[l] not in counter_s1:
                l += 1
                continue

            # Check the window of length s1 starting at l
            window = s2[l : l + n1]
            if Counter(window) == counter_s1:
                return True
            l += 1
        return False