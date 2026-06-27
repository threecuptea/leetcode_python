# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/description
from typing import List
from collections import defaultdict
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref, ans = [0], 0
        lt = defaultdict(int)
        lt[1] = 1 # initial 0
        # [1, 2, 2, 3], [0, -1, 0, 1, 0]
        for num in nums:
            val = pref[-1] + 1 if num == target else pref[-1] - 1
            pref.append(val)
            # print(f'{num}, val= {val}')
            # not initialize it yet
            if lt[val + 1] == 0:
                # can be initialize by the previously accum count + 1
                if lt[val] > 0:
                    lt[val + 1] = lt[val] + 1
                else:
                    lt[val + 1] = 1
                    curr = val + 1
                    while lt[curr + 1] > 0:
                        lt[curr + 1] += 1
                        curr += 1
                    del lt[curr + 1]
            else:
                lt[val + 1] += 1
                curr = val + 1
                while lt[curr + 1] > 0:
                    lt[curr + 1] += 1
                    curr += 1
                del lt[curr + 1]
                # print(dict(lt))
            if lt[val] > 0:
                # print(f'Add {lt[val]}')
                ans += lt[val]
            else:
                del lt[val]
        return ans