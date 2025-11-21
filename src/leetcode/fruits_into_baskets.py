from collections import defaultdict
from typing import List
class Solution:
    ######
    # 904. Fruit Into Baskets
    # https://leetcode.com/problems/fruit-into-baskets/description/
    ######
    # This is a typical sliding window issue
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        max_c, total, l = 0, 0, 0
        # Let r go through the range and l to move to the right to shrink the window if types in count > 2
        for r in range(len(fruits)):
            total += 1
            count[fruits[r]] += 1
            while len(count) > 2:
                total -= 1
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            max_c = max(max_c, total)

        return max_c