from collections import Counter
from typing import List
class Solution:
    # https://leetcode.com/problems/generate-parentheses/
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []
        def what_avail_now():
            counter = Counter(sol)
            if counter['('] == n:
                return [')']
            elif counter['('] == counter[')']:
                return ['(']
            else:
                return ['(', ')']
        def dfs(idx):
            if idx == n * 2:
                ans.append(''.join(sol))
                return
            for ab in what_avail_now():
                sol.append(ab)
                dfs(idx + 1)
                sol.pop()

        dfs(idx= 0)
        return ans