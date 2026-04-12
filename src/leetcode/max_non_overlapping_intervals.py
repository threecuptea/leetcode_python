# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/maximum-non-overlapping-intervals/problem
def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    if len(meetings) in [0, 1]:
        return len(meetings)
    meetings.sort(key= lambda x: x[1])
    count,last_end = 0, -1
    for start, end in meetings:
        if start < last_end:
            continue
        count, last_end = count + 1, end

    return count