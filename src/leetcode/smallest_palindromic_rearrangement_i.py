# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        counter = Counter(s)
        items = sorted(counter.items(), key= lambda item: item[0]) # sort alphabetically
        mid_char = ''
        half = []
        for val, count in items:
            # The value with odd count must sit in the middle
            if count % 2 == 1:
                mid_char = val
            half.extend([val] * (count // 2))
        half_str = ''.join(half)
        return half_str + mid_char + half_str[::-1]