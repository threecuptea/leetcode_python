import heapq
from collections import defaultdict
#
# Complete the 'calculateMinimumSpanningTreeWeightWithFreeEdge' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/min-spanning-tree-with-one-free-edge/problem
def calculateMinimumSpanningTreeWeightWithFreeEdge(n, m, edges):
    # Write your code here
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    min_weight = {}
    min_heap = []
    heapq.heapify(min_heap)
    heapq.heappush(min_heap, (0, 0))

    while min_heap:
        weight_to_i, i = heapq.heappop(min_heap)
        # visited before
        if i in min_weight:
            continue
        min_weight[i] = weight_to_i
        if len(min_weight) == n:
            break
        for nei, nei_weight in g[i]:
            if nei not in min_weight:
                heapq.heappush(min_heap, (nei_weight, nei))

    values = min_weight.values()
    return sum(values) - max(values)