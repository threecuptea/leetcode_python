from typing import (
    List,
)
from collections import defaultdict
# https://neetcode.io/problems/count-connected-components
class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        visited = set()
        g = defaultdict(list)
        for a, b in edges:
            # it needs to be true edge
            if a != b:
                g[a].append(b)
                g[b].append(a)
        num_conn = 0
        # need from node to avoid circular
        def dfs(fr, i):
            visited.add(i)
            for nei in g[i]:
                if nei != fr and nei not in visited:
                    dfs(i, nei)

        for i in range(n):
            if i not in visited:
                num_conn += 1
                dfs(i, i)
        return num_conn