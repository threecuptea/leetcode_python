# From HackRank
def findZeroSumTripletsInWindow(readings, windowSize):
    # Write your code here
    n = len(readings)
    result = set()
    for i in range(n):
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