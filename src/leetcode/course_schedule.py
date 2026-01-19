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
        UNVISIT, VISITING, VISITED = 0, 1, 2
        state = [UNVISIT] * numCourses
        def dfs(c):
            # cycled
            if state[c] == VISITING:
                return False
            elif state[c] == VISITED:
                return True

            state[c] = VISITING
            for p in g[c]:
                if not dfs(p):
                    return False
            state[c] = VISITED
            return True
        # Cannot finish if cycled
        for i in range(numCourses):
            if state[i] == VISITED:
                continue
            if not dfs(i):
                return False
        return True