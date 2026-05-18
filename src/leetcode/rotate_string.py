class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        if len(s) != len(goal):
            return False
        for idx in range(1, len(s)):
            # rotation point, ex. s = "abcde", goal = "cdeab" idx = 2
            if s[idx:] + s[:idx] == goal:
                return True
        return False