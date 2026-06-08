# leetcode.com/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        palindrome, l = s[0], 0
        while True:
            len_p = len(palindrome)
            # the max len of palindro can be is the same as the current palindro. n - 1 -l + 1, need <
            if (n - l) <= len_p:
                break
            # Go backward, hit longest first, (limit - l + 1 = len_p), the boundary
            for r in range(n - 1, len_p - 1 + l, -1):
                sub = s[l:r + 1]
                if sub == sub[::-1]:
                    if len(sub) > len_p:
                        palindrome = sub
                        break
            # l need to increment either when getting new palindro or finish the loop; otherwise it is infinitive loop
            l += 1
        return palindrome