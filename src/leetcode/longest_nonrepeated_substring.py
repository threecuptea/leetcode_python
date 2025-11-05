class Solution:
    ######
    # 3. Longest Substring Without Repeating Characters
    #  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    ####
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        longest = 0
        l = 0
        # r in range deals with window expanding
        for r in range(len(s)):
            # It's a sliding window issue. shrink the window by move l right if it is invalid set,
            # expand the window if it is valid set by moving r right
            # It is inspired by Greg Hogg's YouTube video https://www.youtube.com/watch?v=FCbOzdHKW18
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            w = r - l + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest

def main():
    s = "abcabcbb"
    print(f'Input= {s}')
    solution = Solution()
    output = solution.lengthOfLongestSubstring(s)
    print(f'Output= {output}')

    s = "bbbbb"
    print(f'Input= {s}')
    output = solution.lengthOfLongestSubstring(s)
    print(f'Output= {output}')


if __name__ == "__main__":
    main()