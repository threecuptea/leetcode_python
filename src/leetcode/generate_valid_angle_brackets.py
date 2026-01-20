from collections import Counter
#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/generate-valid-angle-bracket-sequences/problem
#
def generateAngleBracketSequences(n):
    # Write your code here
    # Find what angle brackets are available given the prior bracket sequence
    # There are a couple of rules, number of '<' must be > number of >. For n == 3, you can only use exactly 3 '<' and 3 '>'
    # ab_cnt_dict = {'<': 0, '>': 0}
    ans, sol = [], []
    def what_avail_now():
        counter = Counter(sol)
        if counter['<'] == n:
            return ['>']
        elif counter['<'] == counter['>']:
            return ['<']
        else:
            return ['<', '>']
    def dfs(idx):
        if idx == n * 2:
            ans.append(''.join(sol))
            return
        for ab in what_avail_now():
            sol.append(ab)
            dfs(idx + 1)
            sol.pop()

    dfs(idx= 0)
    return ans