# From HackRank
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/zero-sum-triplets-within-sliding-window/problem
def findZeroSumTripletsInWindow(readings, windowSize):
    # Write your code here
    n = len(readings)
    result = set()
    for i in range(n):
        # Create window of windowSize then use threesum implementation in those windows.
        # Since threesum need to be sorted, it won't maintain existing i, j, k order.  However,
        # We can move l, r to shrink/ expand the sum since they are sorted.
        end = min(i + windowSize, n)
        window = readings[i:end]
        window.sort()
        m = len(window)
        for a in range(m - 2):
            if a > 0 and window[a] == window[a - 1]:
                continue
            if window[a] > 0:
                break
            l, r = a + 1, m - 1
            while l < r:
                tot = window[a] + window[l] + window[r]
                if tot == 0:
                    # Windows are sorted. Any triplets generated from a window are sorted. Append triplets to 'set' to
                    # de-deduplicate.  However, list is not hashable and cannot be used as a key. We need to implement triplets
                    # using tuple, then convert to [] in the result.  That's the trick
                    result.add((window[a], window[l], window[r]))
                    while l < r and window[l] == window[l + 1]:
                        l += 1
                    while l < r and window[r] == window[r - 1]:
                        r -= 1
                    l, r = l + 1, r - 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1

    return [list(tup) for tup in result]

if __name__ == "__main__":
    print(findZeroSumTripletsInWindow([1, -2, 1, -3, 5], 4))