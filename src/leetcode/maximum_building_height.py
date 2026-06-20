# https://leetcode.com/problems/maximum-building-height/description/
from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Building of every increasing heights, build # 1 has height 0
        if len(restrictions) == 0:
            return n - 1
        r = restrictions
        # lower bound
        r.append([1, 0])
        r.sort()
        # upper bound, take the restruction if idx = n has retrictions; otherwise take  n -1
        if r[-1][0] != n:
            r.append([n, n - 1])
        m = len(r)
        # i = 0, [1, 0], it does adjust m - 1, adjust r taking the previous retriction into consideration
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + r[i][0] - r[i - 1][0])
        # i = m - 1, n -1 or r[-1], adjust r taking the next retriction into consideration
        for i in range(m - 2, 0, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + r[i + 1][0] - r[i][0])
        ans = 0
        # I have similar approach up the the last section
        # (best(i, j) - limit(i)) + (best(i, j) - limit(j)) <= j - i, the peak is at the best
        # (j - i) + limit(i) + limit(j) = 2 * best(i, j)
        # idx  5  6  7  8  9
        # val  4  5  6  7  6
        for i in range(m - 1):
            ans = max(ans, (r[i][1] + r[i + 1][1] + (r[i + 1][0] - r[i][0])) // 2)

        return ans
