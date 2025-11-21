
import heapq
from typing import List
class Solution:
    ######
    # 253. Meeting Rooms II
    # https://leetcode.com/problems/number-of-flowers-in-full-bloom/
    ######
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)
        people = [(p, i) for i, p in enumerate(people)]
        result = [0] * len(people)
        cnt = 0
        # need to sort people; otherwise people will be all over the place and cannot share count,
        # start and end (need to make a copy)
        for p, i in sorted(people):
            while start and p >= start[0]:
                heapq.heappop(start)
                cnt += 1
            # end=6, p = 7, pop and decrement
            while end and p > end[0]:
                heapq.heappop(end)
                cnt -= 1
            result[i] = cnt
        return result
