from typing import List

class Solution:
    #####
    # Q1. Find Missing Elements©leetcode
    # https://leetcode.com/contest/weekly-contest-474/problems/find-missing-elements/description/
    #
    ####
    def findMissingElements(self, nums: List[int]) -> List[int]:
        st = sorted(nums)
        missing = []
        prev = 0
        for num in st:
            if prev != 0 and num - prev > 1:
                prev += 1
                while prev < num:
                    missing.append(prev)
                    prev += 1
            prev = num
        return missing