from typing import List
class Solution:
    #####
    # 2187. Minimum Time to Complete Trips
    # https://leetcode.com/problems/minimum-time-to-complete-trips/description/
    ####
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check_status(hrs):
            trips = 0
            for hr in time:
                trips += hrs // hr
            return trips >= totalTrips

        l, r = 0, totalTrips * min(time) + 1
        while True:
            mid = (l + r) // 2
            # mid is long enough to finish those trip, move to the left half
            if check_status(mid):
                r = mid
            # mid is too short finish those trip, move to the right half
            else:
                l = mid
            if  l >= r -1:
                # need to return r because r can finish trips and l fall short
                return r