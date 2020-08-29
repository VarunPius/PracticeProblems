# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
        inorder(root)

        def generateBST(nodes):
            if not nodes:
                return None
            mid = len(nodes)//2
            node = nodes[mid]
            node.left = generateBST(nodes[:mid])
            node.right = generateBST(nodes[mid + 1:])
            return node

        return generateBST(nodes)
