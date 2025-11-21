from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ######
    # 102. Binary Tree Level Order Traversal
    # https://leetcode.com/problems/binary-tree-level-order-traversal/description/
    ######
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        dq = deque([root])
        while dq:
            level = []
            for i in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            result.append(level)
        return result