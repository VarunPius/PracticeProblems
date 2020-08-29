from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        conn = defaultdict(list)

        def map_nodes(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: map_nodes(child, child.left)
            if child.right: map_nodes(child, child.right)

        map_nodes(None, root)
        bfs = [target.val]
        seen = set(bfs)

        for i in range(K):
            new_level = []
            for q_node in bfs:
                for connected_node in conn[q_node]:
                    if connected_node not in seen:
                        new_level.append(connected_node)
            bfs = new_level
            seen |= set(bfs)

        return bfs

