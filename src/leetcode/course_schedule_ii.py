from collections import defaultdict
from typing import List
class Solution:
    #####
    # 210. Course Schedule II
    # https://leetcode.com/problems/course-schedule-ii/description/
    #####
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # inspired by Greg Hogg's https://www.youtube.com/watch?v=2cpihwDznaw
        orders = []
        g = defaultdict(list)
        UNVISIT, VISITING, VISITED = 0, 1, 2
        for a, b in prerequisites:
            g[a].append(b)
        state = [UNVISIT] * numCourses
        def dfs(c):
            # cycled
            if state[c] == VISITING:
                return False
            if state[c] == VISITED:
                return True
            state[c] = VISITING
            for pre in g[c]:
                if not dfs(pre):
                    return False

            state[c] = VISITED
            orders.append(c)
            return True

        for i in range(numCourses):
            if state[i] == VISITED:
                continue
            if not dfs(i):
                return []
        return orders