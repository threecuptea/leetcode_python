# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/minimum-plans-to-reach-target-bandwidth/problem

def findMinimumPlansForBandwidth(planSizes, targetBandwidth):
    # Write your code here
    n = targetBandwidth
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in planSizes:
            if i >= j:
                dp[i] = min(dp[i], dp[i-j] + 1)

    return  -1 if dp[n] ==  float('inf') else dp[n]