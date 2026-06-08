# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Runtime is around average, memory is not as as good
        n = len(s)
        cnt = n # Include all single cases
        # "abcbaab"
        for i in range(1, n):
            # even cases, in abcba'a'b
            if i - 1 >= 0 and s[i] == s[i - 1]:
                cnt += 1 # count duplicate 'a'
                off = 1
                while i - off - 1 >= 0 and i + off < n and s[i - off - 1] == s[i + off]:
                    cnt += 1
                    off += 1
            # odd cases, ab'c'baab
            off = 1
            while i - off >= 0 and i + off < n and s[i - off] == s[i + off]:
                cnt += 1
                off += 1
        return cnt