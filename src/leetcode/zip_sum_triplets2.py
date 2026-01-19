# From HackRank
def findZeroSumTripletsInWindow(readings, windowSize):
    # Write your code here
    print("This is an error message.", file=sys.stderr)
    if windowSize < 3 or len(readings) < 3:
        return []
    result = set()
    n = len(readings)
    for i in range(n-2):
        for j in range(i+1, min(i+windowSize-1, n-1)):
            for k in range(j+1, min(i+windowSize, n)):
                if (readings[i] + readings[j] + readings[k]) == 0:
                    result.add(tuple(sorted([readings[i], readings[j], readings[k]])))

    return [list(tup) for tup in result]



if __name__ == "__main__":
    print(findZeroSumTripletsInWindow([1, -2, 1, -3, 5], 4))