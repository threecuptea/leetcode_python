from collections import defaultdict
from typing import List
# https://neetcode.io/problems/valid-tree/question
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 0:
            return True
        visited = set()
        g = defaultdict(list)
        for a, b in edges:
            # it needs to be true edge
            if a != b:
                g[a].append(b)
                g[b].append(a)
        # need from node to avoid circular
        def dfs(fr, i):
            # no connected edge, not connected
            if not g[i]:
                return False
            # cycled
            if i in visited:
                return False
            visited.add(i)
            for nei in g[i]:
                if nei != fr and not dfs(i, nei):
                    return False
            return True
        # One round is enough to verify if all are connected and non-cycled
        if not dfs(0, 0):
            return False
        if len(visited) != n:
            return False
        return True