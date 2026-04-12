
import sys
def getBinarySearchTreeHeight(values, leftChild, rightChild):
    # Write your code here
    sys.setrecursionlimit(10**6)
    if len(values) == 0:
        return 0
    def dfs(i):
        print(f'i= {i}', file=sys.stderr)
        if i == -1:
            return 0
        print('from the left', file=sys.stderr)
        left_height = dfs(leftChild[i])
        print('from the right', file=sys.stderr)
        right_height = dfs(rightChild[i])

        print(f'left_height= {left_height}', file=sys.stderr)
        print(f'right_height= {right_height}', file=sys.stderr)
        return 1 + max(left_height, right_height)

    return dfs(0)