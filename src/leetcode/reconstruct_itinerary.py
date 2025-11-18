from collections import defaultdict
from typing import List
class Solution:
    #####
    # 332. Reconstruct Itinerary
    # https://leetcode.com/problems/reconstruct-itinerary/description/
    #####
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for s, d in tickets:
            graph[s].append(d)
        for k in graph.keys():
            graph[k].sort(reverse=True)
        stack = ['JFK']
        res = []
        while len(stack) > 0:
            # Keep in stack until we exhaust all paths.  That's the time that we should
            # pop from the stack
            e = stack[-1]
            if e in graph and len(graph[e]) > 0:
                stack.append(graph[e].pop())
            else:
                res.append(stack.pop())
        return res[::-1]