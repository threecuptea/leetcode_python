# https://www.hackerrank.com/contests/mock-interviews-software-engineer-coding/challenges/string-difference-1-4/problem
def getRemovableIndices(str1, str2):
    # Write your code here
    def form_result(idx):
        result = [idx]
        while idx > 0 and str1[idx] == str1[idx - 1]:
            idx -= 1
            result.append(idx)

        return sorted(result)

    idx, n = 0, len(str2)
    while True:
        if str1[idx] == str2[idx]:
            idx += 1
            if idx == n:
                return form_result(n)
        else:
            # when str1[idx] != str2[idx]
            if str1[idx+1] == str2[idx]:
                return form_result(idx)
            else:
                return [-1]