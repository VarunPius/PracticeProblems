# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return
            if parent and grandparent and grandparent.val%2 == 0:
                self.ans += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)

        self.ans = 0
        dfs(root, None, None)
        return self.ans

"""
Alternate tricky solution:
Intuition
Let children know who their grandparent is.

Explanation
Assume node has parent.val = 1 and grandparent.val = 1.
Recursive iterate the whole tree and pass on the value of parent and grandparent.
Count the node.val when grandparent is even-valued.

Complexity
Time O(N)
Space O(height)

    def sumEvenGrandparent(self, root, p=1, gp=1):
        return self.sumEvenGrandparent(root.left, root.val, p) \
            + self.sumEvenGrandparent(root.right, root.val, p) \
            + root.val * (1 - gp % 2) if root else 0
"""