from collections import defaultdict

# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
def sherlockAndAnagrams(s):
    n = len(s)
    anagram_map = defaultdict(int)
    # the length of substring, the maximum is n - 1
    for l in range(1, n):
        # the starting position
        for st in range(0, n -l + 1):
            sorted_substr = ''.join(sorted(s[st:(st + l)]))
            anagram_map[sorted_substr] += 1

    anagram_count = sum([cnt * (cnt - 1) // 2 for cnt in anagram_map.values() if cnt >= 2])
    return anagram_count