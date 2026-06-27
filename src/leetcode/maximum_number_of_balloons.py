# https://leetcode.com/problems/maximum-number-of-balloons/description
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter_b = Counter('balloon')
        counter_t = Counter(text)
        if any(key not in counter_t for key in counter_b.keys()):
            return 0
        multi = counter_t['b'] // counter_b['b'] # The maximum multi can be
        for m in range(multi, 0, -1):
            if all(counter_t[key] >= cnt * m  for key, cnt in counter_b.items()):
                return m
        return 0