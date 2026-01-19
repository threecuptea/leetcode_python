class Solution:
    #####
    # 20. Valid Parentheses
    # https://leetcode.com/problems/valid-parentheses/description/
    #####
    def isValid(self, s: str) -> bool:
        stack = []
        opening_paren = {')': '(', ']' : '[', '}': '{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack[-1] != opening_paren[char]:
                    return False
                stack.pop()
        if stack:
            return False
        return True
