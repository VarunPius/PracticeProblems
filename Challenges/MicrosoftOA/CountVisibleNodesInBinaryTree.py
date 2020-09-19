"""
In a binary tree, if in the path from root to the node A, there is no node with greater value than A’s, this node A is visible. We need to count the number of visible nodes in a binary tree.

Example 1:

Input:
        5
     /     \
   3        10
  /  \     /
20   21   1

Output: 4
Explanation: There are 4 visible nodes: 5, 20, 21, and 10.

Example 2:

Input:
  -10
	\
	-15
	   \
	   -1

Output: 2
Explanation: Visible nodes are -10 and -1.

"""

def count_visible_nodes(root):
	if not root: return 0
	return traverse(root, float('-inf'))

def traverse(node, max_value):
	if not node: return 0
	visible = 1 if node.val >= max_value else 0
	max_value = max(max_value, node.val)
	return traverse(node.left, max_value) + visible + traverse(node.right, max_value)

# RTC: O(N), Space: O(N)

"""
# Microsoft | OA 2020 | Count Visible Nodes in Binary Tree
# https://leetcode.com/discuss/interview-question/546703/

class Node(object):
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None
    def set_left(self, left):
        self._left = left
    def set_right(self, right):
        self._right = right
    def left(self):
        return self._left
    def right(self):
        return self._right
    def val(self):
        return self._val

def count_visible_nodes(root: Node, current_max_val: int) -> int:
    if root is None:
        return 0
    visible = 1 if root.val() >= current_max_val else 0
    current_max_val = max(current_max_val, root.val())
    return count_visible_nodes(root.left(), current_max_val) + count_visible_nodes(root.right(), current_max_val) + visible
    
    
        
def solution(root):
    # Find the count of visible nodes
    return count_visible_nodes(root, 0)

if __name__ == '__main__':
    root = Node(5)
    root.set_left(Node(3))
    root.set_right(Node(10))
    root.left().set_left(Node(20))
    root.left().set_right(Node(21))
    root.right().set_left(Node(1))
    
    print("Count: %d" % (solution(root)))

"""