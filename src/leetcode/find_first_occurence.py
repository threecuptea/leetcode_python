# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/first-occurrence-in-event-code-log/problem
def findFirstOccurrence(nums, target):
    # Write your code here
    l, n = 0, len(nums)
    r, min_idx = n - 1, n
    while l <= r:
        m = l + (r  - l) // 2
        if nums[m] == target:
            min_idx = min(min_idx, m)
            # assume target is to the left
            r = m - 1
        elif target < nums[m]:
            r = m - 1
        else:
            l = m + 1

    return -1 if min_idx == n else min_idx