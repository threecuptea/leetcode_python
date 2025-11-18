from typing import List
class Solution:
    ######
    # 253. Meeting Rooms II
    # https://leetcode.com/problems/meeting-rooms-ii/description/
    ######
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        i, j = 0, 0
        maxcnt = 0
        cnt = 0
        while i < len(start) and j < len(end):
            if end[j] <= start[i]:
                cnt -= 1
                j += 1
            else:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
                i += 1
        return maxcnt