import sys
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/compute-height-of-bst/problem
######
# n = 7
# values = [4, 2, 6, 1, 3, 5, 7]
# leftChild = [1, 3, 5, -1, -1, -1, -1]
# rightChild = [2, 4, 6, -1, -1, -1, -1]
# 4 is the root and index=0 and the left and right child of 4 is at index=0 of the leftChild and the rightChild
# the left child of 4 has index = 1 which is 2, 2's left child is at index = 1 and right index at 2
# 1, 3, 5, 7 all have leftChild and rightChild -1, -1.  They are leaves with height ( 1 + max(0, 0)).  Build the height from the bottom up
#####
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