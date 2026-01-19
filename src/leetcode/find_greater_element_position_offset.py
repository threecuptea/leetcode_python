# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/next-greater-element-with-offset/problem
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