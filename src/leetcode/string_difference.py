# HackRank
def getRemovableIndices(str1, str2):
    # Write your code here
    n = len(str2)
    result = []
    for i in range(n):
        if str1[i] != str2[i]:
            if str1[i + 1] == str2[i]:
                result.append(i)
                break
            else:
                return [-1]
    # str1 is one character more than str2.  Nothing match prior to the end of str2.  str1 must have an extra chacater
    if not result:
        result.append(n)
    j = result[0]
    while j > 0 and str1[j] == str1[j -1]:
        j -= 1
        result.append(j)

    return sorted(result)  