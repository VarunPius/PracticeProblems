from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node):
        if not node: return

        cur, pal = self.dict_freq[node.val], self.Pal

        self.Pal = self.Pal - 1 if cur == 1 else self.Pal + 1
        self.dict_freq[node.val] = (cur + 1)%2

        if not node.left and not node.right and self.Pal <= 1:
            self.res += 1

        self.dfs(node.left)
        self.dfs(node.right)

        self.Pal, self.dict_freq[node.val] = pal, cur


    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.dict_freq = defaultdict(int)
        self.Pal, self.res = 0, 0
        self.dfs(root)
        return self.res
