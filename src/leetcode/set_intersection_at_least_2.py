from typing import List
class Solution:
    ######
    # 757. Set Intersection Size At Least Two
    # https://leetcode.com/problems/set-intersection-size-at-least-two/description/
    ######
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            # we start from the last interval which has more chance to overlap with
            # with the previous one by choosing from the start
            if t == 0:
                continue
            for p in range(s, s + t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans