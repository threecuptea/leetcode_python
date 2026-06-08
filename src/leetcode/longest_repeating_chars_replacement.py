# https://neetcode.io/problems/longest-repeating-substring-with-replacement/question
# https://leetcode.com/problems/longest-repeating-character-replacement/
# https://www.youtube.com/watch?v=tkNWKvxI3mU
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        if len(s) == 1:
            return 1
        l = 0
        counts = [0] * 26 # represents count of A B C D
        # Use "AABAAC" as an example, k = 0 or 1 or 2
        # window size = 3 [2, 1, 0, 0,.........]
        # In order to make the window valid (all have the same characters), we need to replace at least 1 character
        # However, we cannot do that if window size - max_count > k (# characters allowed be replaced)
        for r in range(len(s)):
            # ord('A') = 65, chr(65) = 'A', hex(65) = 0x41, ord('a') = 97
            # (AAB window-size = 3, max(counts) = 2), I need k >= 1 in order to convert 'B' to 'A'
            #  what's required for replacement > what's allowed
            counts[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len