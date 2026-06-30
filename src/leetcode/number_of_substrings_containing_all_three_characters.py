# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r, cnt, n = 0, 0, 0, len(s)
        freq = [0] * 3
        def contains_all_three():
            return all (f for f in freq)
        for r in range(n):
            freq[ord(s[r]) - ord("a")] += 1
            if r - l >= 2 and contains_all_three():
                cnt += n - r
                if n - l == 3:
                    break
                # shrink
                freq[ord(s[l]) - ord("a")] -= 1
                l += 1
                while r - l >= 2 and contains_all_three():
                    cnt += n - r
                    freq[ord(s[l]) - ord("a")] -= 1
                    l += 1
        return cnt