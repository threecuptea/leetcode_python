
from typing import List
class Solution:
    ######
    # 139. Word Break
    # https://leetcode.com/problems/word-break/description/
    ######
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)  # Baseline
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                # enough characters
                if i + len(w) <= n and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # cars, ['car', 'ca' 'rs'], dp[0] can assigned to False if the word chosen is 'car'
                # There can be multiple choices, car[s] ca[rs] but the former does not work
                # because 's' is not in the dictionary.  Need to check if True before break
                if dp[i]:
                    break
        return dp[0]