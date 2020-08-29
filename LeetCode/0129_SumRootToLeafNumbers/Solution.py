# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        ans = 0
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                ans += value
            if node.left:
                stack.append((node.left, value*10 + node.left.val))
            if node.right:
                stack.append((node.right, value*10 + node.right.val))

        return ans

"""
# dfs + stack
def sumNumbers1(self, root):
    if not root:
        return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return res
    
# bfs + queue
def sumNumbers2(self, root):
    if not root:
        return 0
    queue, res = collections.deque([(root, root.val)]), 0
    while queue:
        node, value = queue.popleft()
        if node:
            if not node.left and not node.right:
                res += value
            if node.left:
                queue.append((node.left, value*10+node.left.val))
            if node.right:
                queue.append((node.right, value*10+node.right.val))
    return res
    
# recursively 
def sumNumbers(self, root):
    self.res = 0
    self.dfs(root, 0)
    return self.res
    
def dfs(self, root, value):
    if root:
        #if not root.left and not root.right:
        #    self.res += value*10 + root.val
        self.dfs(root.left, value*10+root.val)
        #if not root.left and not root.right:
        #    self.res += value*10 + root.val
        self.dfs(root.right, value*10+root.val)
        if not root.left and not root.right:
            self.res += value*10 + root.val
"""