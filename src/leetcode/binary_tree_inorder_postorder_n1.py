
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #####
    # 106. Construct Binary Tree from Inorder and Postorder Traversal
    # https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
    ######
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ## This is the implement w/ runtime O(n^2)
        ## This is inspired by neetcode YouTube video https://www.youtube.com/watch?v=vm63HuIU7kw
        inorderidx = {v:i for i, v in enumerate(inorder)}
        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderidx[root.val]
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root

        return helper(0, len(inorder)-1)

def main():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(f'Input= {inorder}, {postorder}')
    solution = Solution()
    output = solution.buildTree(inorder, postorder)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()