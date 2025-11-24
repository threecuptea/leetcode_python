from typing import List
class Solution:
    ######
    # 757. Set Intersection Size At Least Two
    # https://leetcode.com/problems/set-intersection-size-at-least-two/description/
    ######
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Watch Leetcode video
        # It is sorted by start ascending and end descending
        # (2,4), (2,3).  We would process backword and will process more restrict
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # You choose a maximum of two nums from each intervals
        todo = [2] * len(intervals)
        ans = 0
        # It's greedy approach
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            # we start from the last interval which has more chance to overlap with
            # with the previous one by choosing from the start

            if t == 0:
                continue
            for p in range(s, s + t):
                # See if there is any overlap and reduce toto from all previous interval
                for i, (s0, e0) in enumerate(intervals):
                    # also the last one has highest start.  It definitively later than any previous start.
                    # Therefore, we only need to compare with previous end to know if there is overlapping
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans