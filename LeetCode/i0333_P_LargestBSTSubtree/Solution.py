# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        return

"""
Solution 1:
class SubTree(object):
    def __init__(self, largest, n, min, max):
        self.largest = largest  # largest BST
        self.n = n              # number of nodes in this ST
        self.min = min          # min val in this ST
        self.max = max          # max val in this ST

class Solution(object):
    def largestBSTSubtree(self, root):
        res = self.dfs(root)
        return res.largest
    
    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if root.val > left.max and root.val < right.min:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')
            
        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))
"""

"""
Solution2:
def largestBSTSubtree(self, root):
    def dfs(root):
        if not root:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(root.left)
        N2, n2, min2, max2 = dfs(root.right)
        n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
    return dfs(root)[0]

My dfs returns four values:

    N is the size of the largest BST in the tree.
    If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
    If the tree is a BST, then min and max are the minimum/maximum value in the tree.
"""








