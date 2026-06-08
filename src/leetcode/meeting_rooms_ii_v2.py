

from collections import defaultdict
from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    # This is more straightforward but not as efficient as it can be because of two loops
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        check_points = set()
        for intv in intervals:
            check_points.add(intv.start)
            check_points.add(intv.end)
        time_dict = defaultdict(int) # count
        s_timeline = sorted(check_points)
        for intv in intervals:
            for tl in s_timeline:
                if intv.start <= tl and intv.end > tl:
                    time_dict[tl] += 1

        return max([cnt for _, cnt in time_dict.items()])