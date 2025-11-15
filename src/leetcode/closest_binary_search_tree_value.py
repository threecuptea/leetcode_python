from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    #####
    # 270. Closest Binary Search Tree Value
    # https://leetcode.com/problems/closest-binary-search-tree-value/description/
    #####
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = float('inf')
        final = -1
        node = root
        while node:
            if node.val == target:
                return node.val
            diff = abs(node.val - target)
            if diff < min_diff or (diff == min_diff and node.val < final):
                min_diff, final = diff, node.val
            if target < node.val:
                node = node.left
            elif target > node.val:
                node = node.right

        return final