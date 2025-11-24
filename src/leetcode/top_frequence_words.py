from collections import Counter
from typing import List
class Solution:
    ####
    # 692. Top K Frequent Words
    # https://leetcode.com/problems/top-k-frequent-words/description/
    ###
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return [x for x, _ in sorted(c.items(), key=lambda item: (-item[1], item[0]))[:k]]

