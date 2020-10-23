# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode, mn=100000, mx=0) -> int:
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(root.val, mx)), \
                   self.maxAncestorDiff(root.right, min(mn, root.val), max(root.val, mx))) \
                    if root else mx - mn


"""
class Solution(object):
    def maxAncestorDiff(self, root):
        ""
        :type root: TreeNode
        :rtype: int
        ""
        if not root: return 0
        return self.helper(root, root.val, root.val)
    
    def helper(self, node, high, low):
        if not node:
            return high - low
        high = max(high, node.val)
        low = min(low, node.val)
        return max(self.helper(node.left, high, low), self.helper(node.right,high,low))
"""