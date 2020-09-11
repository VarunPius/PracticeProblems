from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build(None)

    def buildTreeRecursive(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTreeRecursive(preorder, inorder[0:ind])
            root.right = self.buildTreeRecursive(preorder, inorder[ind+1:])
            return root

    def buildIterative(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        head = TreeNode(preorder[0])
        stack = [head]
        i = 1
        j = 0

        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1

        return head


"""
Explanation/Discussion:

Consider this input:

preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]
The obvious way to build the tree is:
- Use the first element of preorder, the 1, as root.
- Search it in inorder.
- Split inorder by it, here into [4, 2, 5] and [6, 3].
- Split the rest of preorder into two parts as large as the inorder parts, here into [2, 4, 5] and [3, 6].
- Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
- Use preorder =[3, 6]andinorder = [6, 3] to add the right subtree.

But consider the worst case for this: A tree that's not balanced but is just a straight line to the left.
Then inorder is the reverse of preorder, and already the cost of step 2, searching in inorder, is O(n^2) overall.
Also, depending on how you "split" the arrays, you're looking at O(n^2) runtime and possibly O(n^2) space for that as well.

You can bring the runtime for searching down to O(n) by building a map from value to index before you start the main work, and I've seen several solutions do that.
But that is O(n) additional space, and also the splitting problems remain.
To fix those, you can use pointers into preorder and inorder instead of splitting them. And when you're doing that, you don't need the value-to-index map, either.

Consider the example again. Instead of finding the 1 in inorder, splitting the arrays into parts and recursing on them, just recurse on the full remaining arrays and stop when you come across the 1 in inorder.
That's what my above solution does. Each recursive call gets told where to stop, and it tells its subcalls where to stop.
It gives its own root value as stopper to its left subcall and its parent`s stopper as stopper to its right subcall.

Language details:
About the Python solution:
I'm not sure there's a good way to have those p and i pointers that I use in my Javascript solution, so instead I opted for popping elements from preorder and inorder.
Since popping from the front with pop(0) is expensive O(n), I reverse them before I start so I can use the cheap O(1) popping from the back.


"""
