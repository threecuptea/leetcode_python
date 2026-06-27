# https://leetcode.com/problems/maximum-ice-cream-bars/description/
from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        prev = 0
        for idx, cost in enumerate(costs, start = 1):
            curr = cost + prev
            if curr > coins:
                return idx - 1 # previous index
            prev = curr
        return len(costs)