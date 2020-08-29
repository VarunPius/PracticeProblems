# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.numOfPaths = 0

        self.dfs(root, sum)
        return self.numOfPaths

    def dfs(self, node, target):
        if node is None:
            return

        self.calculate(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def calculate(self, node, target):
        if node is None:
            return

        if node.val == target:
            self.numOfPaths += 1

        self.calculate(node.left, target - node.val)
        self.calculate(node.right, target - node.val)
