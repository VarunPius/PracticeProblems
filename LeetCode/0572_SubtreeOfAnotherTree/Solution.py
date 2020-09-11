# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def isSubtree(self, s, t):
        if not s:
            return False
        if self.isMatch(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        # if not (s and t):         # to evaluate; try alternative below
        #    return s is t

        if (s is None and t is not None) or (s is not None and t is None):
            return False
        elif s is None and t is None:
            return True

        return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)


"""
Naive approach, O(|s| * |t|)
For each node of s, let's check if it's subtree equals t.
We can do that in a straightforward way by an isMatch function:
check if s and t match at the values of their roots, plus their subtrees match.
Then, in our main function, we want to check if s and t match, or if t is a subtree of a child of s.
"""

"""
Alternate Approach:
O(|s| + |t|) (Merkle hashing):
For each node in a tree, we can create node.merkle, a hash representing it's subtree.
This hash is formed by hashing the concatenation of the merkle of the left child, the node's value, and the merkle of the right child.
Then, two trees are identical if and only if the merkle hash of their roots are equal (except when there is a hash collision.)
From there, finding the answer is straightforward: we simply check if any node in s has node.merkle == t.merkle
"""

from hashlib import sha256

def isSubtree(self, s, t):
    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()

    def merkle(node):
        if not node:
            return '#'
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        return node.merkle

    merkle(s)
    merkle(t)

    def dfs(node):
        if not node:
            return False
        return (node.merkle == t.merkle or
                dfs(node.left) or dfs(node.right))

    return dfs(s)
