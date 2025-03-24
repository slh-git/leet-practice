from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # if the diff is true and every child node is also true
            if abs(left[1] - right[1]) <= 1 and left[0] and right[0]:
                return [True, 1 + max(left[1], right[1])]
            # at least one of them isnt balanced
            return [False, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# NOTE:
# Time = O(n)
# Space = O(h) balanced case O(logn) worse case O(n)
