from typing import List
class Solution:
    # https://leetcode.com/problems/combination-sum/
    # Inspired by Greg Hoggs's https://www.youtube.com/watch?v=utBw5FbYswk
    # https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-index-combinations-target-weight/problem
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = [2,3,6,7], target = 7, the answer is [2, 2, 3] or [7], Since we can use the same index
        # multiple time.  The decision is to advance and not to choose or to choose that index
        res, sol = [], []
        nums = candidates
        n = len(nums)
        def backtrack(idx, cur_sum):
            if cur_sum == target:
                res.append(sol[:]) # sol will be subject to change
                return
            if cur_sum > target or idx == n:
                return
            # not to use the cur_idx, no cost to include in curr_sum
            backtrack(idx+1, cur_sum)

            sol.append(nums[idx])
            backtrack(idx, cur_sum + nums[idx])
            sol.pop()

        backtrack(0, 0)
        return res