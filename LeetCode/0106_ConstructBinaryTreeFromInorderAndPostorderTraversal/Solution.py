# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder:
            return None

        map_inorder = {}

        for i, val in enumerate(inorder): map_inorder[val] = i

        def recur(low, high):
            if low > high: return None

            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid + 1, high)
            x.left = recur(low, mid - 1)
            return x

        return recur(0, len(inorder) - 1)


"""
Here I copied the top voted Python solution:

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val) # Line A

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder) # Line B
        root.left = self.buildTree(inorder[:inorderIndex], postorder) # Line C

        return root
The code is clean and short. However, if you give this implementation during an interview, there is a good chance you will be asked, "can you improve/optimize your solution?"

Why? Take a look at Line A, Line B and Line C.
Line A takes O(N) time.
Line B and C takes O(N) time and extra space.
Thus, the overall running time and extra space is O(N^2).
So this implementation has a very bad performance, and you can avoid it.

That is why the above solution which has O(N) time and extra space.
"""