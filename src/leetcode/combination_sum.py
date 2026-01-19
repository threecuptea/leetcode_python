from typing import List
class Solution:
    # https://leetcode.com/problems/combination-sum/
    # Inspired by Greg Hoggs's https://www.youtube.com/watch?v=utBw5FbYswk
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums = candidates
        n = len(nums)
        def backtrack(idx, cur_sum):
            if cur_sum == target:
                res.append(sol[:]) # sol will be subject to change
                return
            if cur_sum > target or idx == n:
                return
            # not to use the cur_idx
            backtrack(idx+1, cur_sum)

            sol.append(nums[idx])
            backtrack(idx, cur_sum + nums[idx])
            sol.pop()

        backtrack(0, 0)
        return res