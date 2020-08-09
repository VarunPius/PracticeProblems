from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        op = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is not None:
                op.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                op.append("#")
        return ",".join(op)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        #if not data: return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque([root])
        idx = 1
        while q:
            node = q.popleft()
            if data[idx] != "#":
                node.left = TreeNode(int(data[idx]))
                q.append(node.left)
            idx += 1

            if data[idx] != "#":
                node.right = TreeNode(int(data[idx]))
                q.append(node.right)
            idx += 1

        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
'''

if __name__ == '__main__':
    root = TreeNode(1)
    l1 = TreeNode(2)
    r1 = TreeNode(3)
    l2 = TreeNode(4)
    r2 = TreeNode(5)
    root.left = l1
    root.right = r1
    r1.left = l2
    r1.right = r2
    codec = Codec()
    coda = codec.serialize(None)
    print(coda)
    orig = codec.deserialize(coda)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))