from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []

        def dfs(root, lvl):
            if not root:
                return
            if len(out) == lvl:
                out.append([])
            out[lvl].append(root.val)

            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)

        dfs(root, 0)
        return out
