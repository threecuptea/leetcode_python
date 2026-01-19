from collections import Counter, deque
from typing import List
import heapq
class Solution:
    # https://leetcode.com/problems/task-scheduler/
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # https://youtu.be/s8p8ukTyA2I
        # Use max_heap to process the most frequent one first (greedy)
        # AAA BB CC, n = 1
        # BCBCA_A_A vs. ABCABCA
        # need negative numbers for max heap
        max_heap = [ -cnt for cnt in Counter(tasks).values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap) # - 3 + 1
                if cnt:
                    # (cnt, when is available)
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time