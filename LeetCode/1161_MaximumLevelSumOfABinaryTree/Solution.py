# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(node, list, level):
            if not node:
                return
            if len(list) == level:
                list.append(node.val)
            else:
                list[level] += node.val

            dfs(node.left, list, level + 1)
            dfs(node.right, list, level + 1)

        list = []
        dfs(root, list, 0)
        return 1 + list.index(max(list))

"""
#BFS
    def maxLevelSum(self, root: TreeNode) -> int:
        max, level, maxLevel = -float('inf'), 0, 0
        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max < sum:
                max, maxLevel = sum, level        
        return maxLevel
"""