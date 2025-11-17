from collections import defaultdict
from typing import List
class Solution:
    ######
    # 904. Fruit Into Baskets
    # https://leetcode.com/problems/fruit-into-baskets/description/
    ######
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        max_c = 0
        start_idx = 0
        for i, t in enumerate(fruits):
            if (len(d) == 2 and t in d) or len(d) < 2:
                d[t] += 1
            else:
                max_c = max(max_c, sum([val for val in d.values()]))
                while len(d) == 2:
                    start_t = fruits[start_idx]
                    d[start_t] -= 1
                    if d[start_t] == 0:
                        del d[start_t]
                    start_idx += 1
                d[t] += 1
        if d:
            max_c = max(max_c, sum([val for val in d.values()]))
        return max_c