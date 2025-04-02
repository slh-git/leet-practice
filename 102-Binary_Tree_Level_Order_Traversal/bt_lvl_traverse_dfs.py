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

        def dfs(node, level):
            if not node:
                return None
            if len(out) == level:
                out.append([])
            out[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return out


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
