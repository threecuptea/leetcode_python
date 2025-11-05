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
        if not inorder:
            return None
        ### This is the implement w/ runtime O(n^2)
        ## This is inspired by neetcode YouTube video https://www.youtube.com/watch?v=vm63HuIU7kw
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root

def main():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(f'Input= {inorder}, {postorder}')
    solution = Solution()
    output = solution.buildTree(inorder, postorder)
    print(f'Output= {output}')

if __name__ == "__main__":
    main()