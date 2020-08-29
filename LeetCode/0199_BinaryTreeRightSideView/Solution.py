# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def rightSideView(self, root: TreeNode) -> List[int]:
    def rightSideView(self, root: TreeNode):
        ans = []
        self.dfs(root, 0, ans)
        return [x[0] for x in ans]

    def dfs(self, node, lvl, ans):
        if node:
            if len(ans) < lvl + 1:
                ans.append([])

            ans[lvl].append(node.val)
            self.dfs(node.right, lvl + 1, ans)
            self.dfs(node.left, lvl + 1, ans)


"""
# DFS recursively
def rightSideView(self, root):
    res = []
    self.dfs(root, 0, res)
    return [x[0] for x in res]
    
def dfs(self, root, level, res):
    if root:
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.right, level+1, res)
        self.dfs(root.left, level+1, res)

# DFS + stack
def rightSideView2(self, root):
    res, stack = [], [(root, 0)]
    while stack:
        curr, level = stack.pop()
        if curr:
            if len(res) < level+1:
                res.append([])
            res[level].append(curr.val)
            stack.append((curr.right, level+1))
            stack.append((curr.left, level+1))
    return [x[-1] for x in res]
        
# BFS + queue
def rightSideView(self, root):
    res, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if curr:
            if len(res) < level+1:
                res.append([])
            res[level].append(curr.val)
            queue.append((curr.left, level+1))
            queue.append((curr.right, level+1))
    return [x[-1] for x in res]
"""