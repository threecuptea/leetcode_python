# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    #######
    # 105. Construct Binary Tree from Preorder and Inorder Traversal
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
    #######
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # preorder: the node first, the left node, then the right node.  The root is always preorder[0]
        # inorder means nodes are in order: the left node, the node itself, the right node
        # buildTree left and right and how to use mid is pretty intuitive
        # It is inspired by neetcode YouTube video https://www.youtube.com/watch?v=ihj4IQGZ2zc
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(f'Input= {preorder}, {inorder}')
    solution = Solution()
    output = solution.buildTree(preorder, inorder)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()

