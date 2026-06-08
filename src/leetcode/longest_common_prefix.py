# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the longest common prefix can be
        min_len = min([len(st) for st in strs])
        # ["flower","flow","flight"]
        # the last one is [:1], one character
        for end in range(min_len, 0, -1):
            prefix = strs[0][:end]
            any_not_equal = any(st[:end] != prefix for st in strs[1:])
            if not any_not_equal:
                return prefix
        return ""