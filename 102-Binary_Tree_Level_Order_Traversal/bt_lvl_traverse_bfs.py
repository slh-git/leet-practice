from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            q_len = len(queue)
            lvl = []
            for _ in range(q_len):
                curr = queue.popleft()
                if curr:
                    lvl.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)

            # if list not empty append to out
            if lvl:
                out.append(lvl)

        return out
