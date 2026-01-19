# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
def maximumSum(a, m):
    # Write your code here
    prefix_sum = [(0, -1)]
    for i in range(len(a)):
        prefix_sum.append(((prefix_sum[-1][0]+a[i])%m, i))

    prefix_sum.sort()
    # maximum has maximum module of the sum of index=0 up to index=i
    # [3, 3, 9, 9, 5], prefix_sum before sorted[(0,-1),(3,0),(6,1),(1,2),(3,3),(1,4)]
    # After sorted [(0,-1),(1,2),*(1,4),(3,0),**(3,3),(6,1)]
    # zip with     [(1,2), (1,4),*(3,0),(3,3),**(6,1)]
    maximum = prefix_sum[-1][0]
    # short cut, it cannot be bigger than that
    if maximum == m -1:
        return maximum
    for (m1, idx1), (m2, idx2) in zip(prefix_sum[:-1], prefix_sum[1:]):
        # This might be a tricky way to find teh maximum
        # Those stars are candidate pair, (1,4) - (3,0), [0:5](3 3 9 9 5) - [0:1] (3) = 3 9 9 5 its module (1-3 + 7) = 5
        if m1 < m2 and idx1 > idx2:
            maximum = max(maximum, m1 - m2 + m)
    return maximum