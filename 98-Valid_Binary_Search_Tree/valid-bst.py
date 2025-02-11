from typing import Optional
# O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # NOTE: Not left and right node but left and right BOUNDARY see diagram
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            # NOTE: check update left boundary < left node < curr node value AND
            #       current node < right node < right bound
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))
