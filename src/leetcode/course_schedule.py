from collections import defaultdict
from typing import List
class Solution:
    #####
    # 207. Course Schedule
    # https://leetcode.com/problems/course-schedule/description/
    #####
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(c):
            # cycled
            if states[c] == VISITING:
                return False
            elif states[c] == VISITED:
                return True

            states[c] = VISITING
            for p in g[c]:
                if not dfs(p):
                    return False
            states[c] = VISITED
            return True
        # Cannot finish if cycled
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True