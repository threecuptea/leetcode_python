# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/merge-and-sort-intervals/problem
def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    if len(intervals) < 2:
        return intervals
    intervals.sort(key = lambda e: e[0])
    combined = []
    for st, end in intervals:
        if not combined:
            combined.append([st, end])
        else:
            last_start, last_end = combined[-1]
            if st <= last_end:
                last_start, last_end = combined.pop()
                comb_end = max(last_end, end)
                combined.append([last_start, comb_end])
            else:
                combined.append([st, end])

    return combined
