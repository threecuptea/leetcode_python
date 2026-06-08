class Solution:
    ######
    # 3. Longest Substring Without Repeating Characters
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    ####
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        sett = set(s[0])
        l, max_len = 0, 1
        for r in range(1, n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len

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