import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def preorder(node):
            if node:
                vals.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(minValue, maxValue):
            if vals and minValue < vals[0] < maxValue:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minValue, val)
                node.right = build(val, maxValue)
                return node

        return build(float('-infinity'), float('infinity'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))