
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-number-pairs/problem
def countAffordablePairs(prices, budget):
    # Write your code here
    total = 0
    for l in range(len(prices)-1):
        r = len(prices)-1
        while r > l and prices[l] + prices[r] > budget:
            r -= 1
        total += (r - l)

    return total
