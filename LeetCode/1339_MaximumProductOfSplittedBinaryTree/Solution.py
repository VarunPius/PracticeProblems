# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums = []
        def fn(node):
            if not node: return 0
            ans = node.val + fn(node.left) + fn(node.right)
            sums.append(ans)
            return ans

        total = fn(root)
        return max((x * (total - x)) for x in sums) % (10**9+7)
