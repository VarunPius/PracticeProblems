# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
    def boundaryOfBinaryTree(self, root: TreeNode):
        return


"""
Solution 1: DFS
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary
"""

"""
Solution 2:
# Let's merely get the nodes from the left boundary, the right boundary, and the leaves, in counter-clockwise order.
# 
# To get nodes from the left boundary, we start from root.left and move left if we can, else right, until we can't move anymore. 
# The right boundary is similar.
# 
# To get nodes from the leaves, we DFS until we hit a leaf (until node.left and node.right are both None). 
# We should take care to add to our stack in the order (right, left) so that they are popped in the order (left, right).
# 
# Now armed with all the nodes we could visit, let's visit them in order. 
# As we visit a node, we should skip over ones we've seen before (comparing node objects by pointer, not node.val), and otherwise add node.val to our answer.
# 
# We could also rewrite this answer by calling visit(cur) directly instead of appending to left_bd_nodes, etc. to save a little space.

if not root: return []

left_bd_nodes = [root]
cur = root.left
while cur:
  left_bd_nodes.append(cur)
  cur = cur.left or cur.right

right_bd_nodes = [root]
cur = root.right
while cur:
  right_bd_nodes.append(cur)
  cur = cur.right or cur.left

leaf_nodes = []
stack = [root]
while stack:
  node = stack.pop()
  if node.right:
    stack.append(node.right)
  if node.left:
    stack.append(node.left)
  if not node.left and not node.right:
    leaf_nodes.append(node)

ans = []
seen = set()
def visit(node):
  if node not in seen:
    seen.add(node)
    ans.append(node.val)

for node in left_bd_nodes: visit(node)
for node in leaf_nodes: visit(node)
for node in reversed(right_bd_nodes): visit(node)

return ans
"""

"""
Solution3: Recursive DFS
def boundaryOfBinaryTree(self, root):
    # The main idea is to carry the flag isleft and isight
    # in the dfs steps to help decide when to add node
    # values to the boundary array.
    if not root: return []
    boundary = [root.val]
    def dfs(root, isleft, isright):
        if root:
            # append when going down from the left or at leaf node
            if (not root.left and not root.right) or isleft:
                boundary.append(root.val)
            
            if root.left and root.right:
                dfs(root.left, isleft, False)
                dfs(root.right, False, isright)
            else:
                dfs(root.left,  isleft, isright)
                dfs(root.right, isleft, isright)
            
            # append to boundary when coming up from the right
            if (root.left or root.right) and isright:
                boundary.append(root.val)
    
    dfs(root.left, True, False)
    dfs(root.right, False, True)
    return boundary
"""