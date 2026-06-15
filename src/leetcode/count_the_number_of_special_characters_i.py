# https://leetcode.com/problems/count-the-number-of-special-characters-i/
from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        if len(word) == 1:
            return 0
        dd = defaultdict(set)
        for ch in word:
            dd[ch.lower()].add(ch)

        return sum([len(lst) - 1 for _, lst in dd.items()])