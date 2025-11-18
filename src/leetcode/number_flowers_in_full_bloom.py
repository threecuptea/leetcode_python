from sortedcontainers import SortedDict
from typing import List
class Solution:
    ######
    # 253. Meeting Rooms II
    # https://leetcode.com/problems/number-of-flowers-in-full-bloom/
    ######
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # My own implementation
        start = sorted([x[0] for x in flowers])
        end = sorted([(x[1]+1) for x in flowers])
        i, j, cnt = 0, 0, 0
        result = []
        sd = SortedDict()
        while i < len(start) and j < len(end):
            # end is inclusive
            if end[j] == start[i]:
                i += 1
                j += 1
            elif end[j] < start[i]:
                cnt -= 1
                sd[end[j]] = cnt
                j += 1
            else:
                cnt += 1
                sd[start[i]] = cnt
                i += 1
        while j < len(end):
            cnt -= 1
            sd[end[j]] = cnt
            j += 1

        n = len(sd)
        for i, p in enumerate(people):
            l = sd.bisect_left(p)
            r = sd.bisect_right(p)
            # not found
            if l == 0 and r == 0:
                result.append(0)
            elif l == n:
                result.append(sd.peekitem(n - 1)[1])
            elif l == r:
                # in between
                result.append(sd.peekitem(l - 1)[1])
            else:
                result.append(sd.peekitem(l)[1])
        return result
