
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tmp = Node(-1)
        cur = tmp
        ans = root
        while root:
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = tmp.next
            cur = tmp
            tmp.next = None

        return ans

"""
Above solution is O(1) Space approach

BFS: Level Order Traversal - simple approach:
def connect(self, root: 'Node') -> 'Node':
	if not root:
            return root
        q = []
        
        q.append(root)
        
        tail = root
        while len(q) > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            if node == tail:
                node.next = None
                tail = q[-1] if len(q) > 0 else None
            else:
                node.next = q[0]
                
        return root

"""