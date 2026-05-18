# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # the longest common prefix can be
        min_len = min([len(x) for x in strs])
        n = len(strs)
        for i in range(min_len, 0, -1):
            comp = strs[0][:i]
            any_not_equal = any(s[:i] != comp  for s in strs[1:n])
            if not any_not_equal:
                return comp
        return ""