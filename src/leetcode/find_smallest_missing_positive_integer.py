# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer
def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    if not orderNumbers:
        return 1
    n = len(orderNumbers)
    set_c = set(range(1, n + 1))
    set_o = set(num for num in orderNumbers if num > 0)
    set_diff = set_c - set_o
    if set_diff:
        return sorted(list(set_diff))[0]

    return n + 1