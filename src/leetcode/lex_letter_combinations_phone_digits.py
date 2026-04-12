# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/lexicographical-letter-combinations-phone-digits
def minTasksToCancelForNoConflict(digits):
    # Write your code here
    letter_map = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # sol single char
    ans, sol, n = [], [], len(digits)
    def backtrack(i):
        if i == n:
            ans.append(''.join(sol))
            return
        for letter in letter_map[digits[i]]:
            # push a, backtrack to the next level, digits (i + 1)
            # push d, backtrack again, finish all digits, append('ad') to ans, pop('d'),
            # push e, backtrack will append 'ae' to ans, pop('e'), then process 'f',
            # finish all combinations string starting at 'a', pop('a'), then process 'b'
            sol.append(letter)
            backtrack(i+1)
            sol.pop()

    backtrack(0)
    return sorted(ans)