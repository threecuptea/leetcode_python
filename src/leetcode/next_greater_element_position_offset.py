# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/next-greater-element-with-offset/problem
"""
Given an integer array readings, return an array result where result[i] = [value, distance], with value being the next greater element to the right of readings[i] and distance being the index difference. If no greater element exists, return [-1, -1].

Input
readings = [2, 1, 2, 4, 3]

Output
[[4, 3], [2, 1], [4, 1], [-1, -1], [-1, -1]]
"""
def findNextGreaterElementsWithDistance(readings):
    # Write your code here
    if not readings:
        return []
    if len(readings) == 1:
        return [[-1, -1]]
    result = [[-1, -1]] * len(readings)
    stack = []

    for idx, val in enumerate(readings):
        while stack and val > stack[-1][0]:
            stk_val, stk_idx = stack.pop()
            result[stk_idx] = [val, idx - stk_idx]
        stack.append((val, idx))

    return result