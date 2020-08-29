from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = deque([(root, 1)])

        while que:
            node, level = que.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    que.append((node.left, level + 1))
                    que.append((node.right, level + 1))

"""
# DFS
def minDepth1(self, root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
"""
