# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0

        def depth(node):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.result

"""
If you think about what depth() is supposed to do, it returns the height of the deepest sub tree of the passed in node p (which is the max of either the left child sub tree or the right child subtree).

If you want a more illustrative way to visualize this, imagine the binary tree in your head and each node has an additional field called depth. The value of this field is the maximum value of the depth field of either it’s left child or it’s right child. The leaves of this tree have depth 1.

Now, the question is asking for the largest diameter of the tree and not the largest depth. So, self.ans (which is what we return at the end) should contain information about the largest diameter observed (which would be the maximum of the previous largest diameter or the current nodes “diameter”, which the sum of the left and right sub trees). That’s why we update it as we recursively iterate over every node in the tree. At the end, we are left with the correct answer in self.ans and we return that. The output of the depth(root) call just returns the maximum depth of the root tree and not the diameter.
"""
