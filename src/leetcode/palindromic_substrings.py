# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Runtime is very good, too many loop.  However, memory is very good
        n, l = len(s), 0
        cnt = 0
        while True:
            cnt += 1
            for r in range(l + 1, n):
                sub = s[l:r + 1]
                if sub == sub[::-1]:
                    cnt += 1
            l += 1
            if l == n:
                break
        return cnt