# https://leetcode.com/problems/count-the-number-of-special-characters-ii/
from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dd = defaultdict(set)
        for ch in word:
            upp = ch.upper()
            # lowercase
            if ord(ch) >= 97 and upp in dd[upp]:
                # Clean it up if I have already put a lower ch before upper ch
                # I cannot clean the upper 'ch'.  I need to keep it as a placeholder to block all the following lower ch
                dd[upp] = set(upp)
            # It will exceed timeout if I don't put the following condition.
            elif ch not in dd[upp]:
                dd[upp].add(ch)
        return sum([1 for _, lst in dd.items() if len(lst) == 2])