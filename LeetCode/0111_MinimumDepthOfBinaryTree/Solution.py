from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = deque([(root, 1)])

        while que:
            node, level = que.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    que.append((node.left, level + 1))
                    que.append((node.right, level + 1))


if __name__ == "__main__":
    root = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node5 = TreeNode(5)

    root.left = node9
    root.right = node20
    node20.left = node15
    node20.right = node7
    node7.left = node5

    soln = Solution()
    x = soln.minDepth(root) 
    print(x)   


"""
# DFS
def minDepth1(self, root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
"""
