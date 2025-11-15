from typing import List
class Solution:
    #######
    # 228. Summary Ranges
    # https://leetcode.com/problems/summary-ranges/description/
    #######
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        dump = []
        for num in nums:
            if dump:
                if num == dump[-1] + 1:
                    dump.append(num)
                else:
                    ## To write out when not finding continuous number
                    if len(dump) == 1:
                        result.append(str(dump[-1]))
                    else:
                        result.append(f'{dump[0]}->{dump[-1]}')
                    dump.clear()
                    dump.append(num)
            else:
                dump.append(num)
        # don't forget to write out the last elements(s) in dump
        if dump:
            if len(dump) == 1:
                result.append(str(dump[-1]))
            else:
                result.append(f'{dump[0]}->{dump[-1]}')
        return result