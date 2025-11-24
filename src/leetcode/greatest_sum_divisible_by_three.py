from collections import defaultdict
from typing import List
class Solution:
    ######
    # 1262. Greatest Sum Divisible by Three
    # https://leetcode.com/problems/greatest-sum-divisible-by-three/description/
    ######
    def maxSumDivThree(self, nums: List[int]) -> int:
        r1 = []
        r2 = []
        total = 0
        for num in nums:
            if num % 3 == 1:
                r1.append(num)
            elif num % 3 == 2:
                r2.append(num)
            total += num
        if total % 3 == 0:
            return total
        r1.sort()
        r2.sort()
        rem = total % 3
        # This approach is pretty shortcut.  Just sort and make best use of modulo
        if rem == 1:
            op1 = total - r1[0] if len(r1) >= 1 else 0
            op2 = total - r2[0] - r2[1] if len(r2) >= 2 else 0
        else:
            op1 = total - r1[0] - r1[1] if len(r1) >= 2 else 0
            op2 = total - r2[0] if len(r2) >= 1 else 0
        return max(op1, op2)