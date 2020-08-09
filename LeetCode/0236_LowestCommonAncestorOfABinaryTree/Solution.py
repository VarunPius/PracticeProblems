# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root

        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        # print("left: ", left.val if left else "LeftNone")
        # print("right: ", right.val if right else "RightNone")
        return root if left and right else left or right

    # Easier code
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # If looking for me, return myself
        if root == p or root == q:
            return root

        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
            # either one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA
            return left or right

if __name__ == '__main__':
    soln = Solution()
    root = TreeNode(3)
    l1 = TreeNode(5)
    r1 = TreeNode(1)
    l1l2 = TreeNode(6)
    l1r2 = TreeNode(2)
    r1l2 = TreeNode(0)
    r1r2 = TreeNode(8)
    l1r2l3 = TreeNode(7)
    l1r2r3 = TreeNode(4)
    root.left = l1
    root.right = r1
    l1.left = l1l2
    l1.right = l1r2
    r1.left = r1l2
    r1.right = r1r2
    l1r2.left = l1r2l3
    l1r2.right = l1r2r3
    x = soln.lowestCommonAncestor(root, l1r2r3, r1r2)
    print("Val: ", x.val)


"""
return root if left and right else left or right 
    can be written as / is equivalent to:
if(left == null && right == null) return null; 
if(left != null && right != null) return root;  
return left == null ? right : left;
"""


"""
NoneType has no val attribute for following:
while True:
    if root.val > node1 and root.val > node2:
        root = root.left
    elif root.val < node1 and root.val < node2:
        root = root.right
    else:
        return root
"""

