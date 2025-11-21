from typing import List
class Solution:
    ######
    # 252. Meeting Rooms
    # https://leetcode.com/problems/meeting-rooms/description/
    ######
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        i, j, cnt = 0, 0, 0
        # Technically we did not go through all end points.  However, it does not matter.
        # cnt can only decrement after we finish all start.  cnt > 1 can only happen when we go through
        # all starting point, if one course ends at the same time as another course starts, will process
        # 'end' first.  In another word, the count will remain the same after all were processed
        while i < len(start) and j < len(end):
            if end[j] <= start[i]:
                cnt -= 1
                j += 1
            else:
                cnt += 1
                if cnt == 2:
                    return False
                i += 1
        return True