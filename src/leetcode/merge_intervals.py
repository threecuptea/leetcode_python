from typing import List

class Solution:
    #####
    # 56. Merge Intervals
    # https://leetcode.com/problems/merge-intervals/description/
    #####
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        result = []
        sorted_i = sorted(intervals, key=lambda r: r[0])  # sorted by start
        result.append(sorted_i[0])
        for curr in sorted_i[1:]:
            prev = result[-1]
            # check overlapping
            if curr[0] <= prev[1]:
                result.pop()
                end = max(curr[1], prev[1])
                result.append([prev[0], end])
            else:
                result.append(curr)
        return result