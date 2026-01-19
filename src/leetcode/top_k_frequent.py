# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/top-k-frequent-events-with-order-preservation/problem?isFullScreen=true
# hackerrank
from collections import Counter
def getTopKFrequentEvents(events, k):
    # Write your code here
    if len(events) == 0 or k == 0:
        return []
    c = Counter(events)
    return [pair[0] for pair in c.most_common(k)]