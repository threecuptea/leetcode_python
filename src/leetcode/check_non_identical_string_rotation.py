from collections import deque
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-non-identical-string-rotation/problem
def isNonTrivialRotation(s1, s2):
    # Write your code here
    if s1 == s2:
        return 0
    dq = deque(s1)
    rotate, n = 0, len(s1)
    while rotate < n:
        dq.append(dq.popleft())
        if ''.join(dq) == s2:
            return 1
        rotate += 1

    return 0