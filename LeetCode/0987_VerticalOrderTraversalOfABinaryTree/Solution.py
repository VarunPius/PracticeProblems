from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    def verticalTraversal(self, root: TreeNode):
        ans = defaultdict(list)
        que = [(root, 0)]

        while que:
            new = []
            dic = defaultdict(list)
            for node, lvl in que:
                dic[lvl].append(node.val)
                if node.left: new.append((node.left, lvl - 1))
                if node.right: new.append((node.right, lvl + 1))

            que = new
            for lvl in dic: ans[lvl].extend(sorted(dic[lvl]))

        return [ans[i] for i in sorted(ans)]

