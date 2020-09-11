# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []
        def helper(node, is_root):
            if not node:
                return None

            node_deleted = node.val in to_delete_set

            if is_root and not node_deleted:
                res.append(node)

            node.left = helper(node.left, node_deleted)
            node.right = helper(node.right, node_deleted)

            return None if node_deleted else node

        helper(root, True)
        return res

"""
Explanation
If a node is root (has no parent) and isn't deleted,
when will we add it to the result.


Complexity
Time O(N)
Space O(H + N), where H is the height of tree.
"""
