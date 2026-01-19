
import sys
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/compute-height-of-bst/problem
def getBinarySearchTreeHeight(values, leftChild, rightChild):
    # Write your code here
    sys.setrecursionlimit(10**6)
    if len(values) == 0:
        return 0
    def dfs(i):
        if i == -1:          # no child
            return 0
        left_height = dfs(leftChild[i])
        right_height = dfs(rightChild[i])
        return 1 + max(left_height, right_height)

    return dfs(0)