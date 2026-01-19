import heapq
from typing import List
from collections import defaultdict
class Solution:
    #####
    # 743. Network Delay Time
    # Djikstra shortestpath algorithm, coding is inspired by Greg Hogg's https://www.youtube.com/watch?v=Bp7STMWMMQw
    # https://leetcode.com/problems/network-delay-time/
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, t in times:
            g[u].append((v, t))
        min_times = {}  # node -> the distance from source
        # Need to keep in order of distance, therefore, the tuple is (total distiance_from_source, node)
        min_heap = [] # put starting node so that we can pop up in distance order
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, (0, k)) # so that we can start heap process

        while min_heap:
            time_to_i, i = heapq.heappop(min_heap)
            # It has visited before, ignore it
            if i in min_times:
                continue
            min_times[i] = time_to_i
            # 1 -> 2 (1), 1 -> 4 (4), 2 -> 3, 1 (1 -> 3:1+1=2), 3 -> 4, 1 (1->4:2+1=3), 1 -> 2 -> 3 -> 4 (3) 4 will be visited via this route
            # first.  when 4 (4) was popped out, it will be ignored because it was visited by previous route
            # 4 will be in the mean_times
            for nei, nei_time in g[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_to_i + nei_time, nei))

        if len(min_times) == n:
            return max(min_times.values())
        # Unable to visit all nodes
        return -1