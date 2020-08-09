from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result, tmp_que, flag = [], [], 1
        que = deque()
        que.append(root)
        # result.append([root.val])

        while que:
            for i in range(len(que)):
                node = que.popleft()
                tmp_que.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if tmp_que:
                result.append(tmp_que[::flag])
            tmp_que = []
            flag *= -1

        return result


"""
we use deque.popleft() and not stack is because stack.pop(0) is O(n) while deque append and pop are O(1).
"""