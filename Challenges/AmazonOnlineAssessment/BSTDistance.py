class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstDistance(num, values, node1, node2):
    # WRITE YOUR CODE HERE
    # build tree
    if not num:
        return -1
    if len(values) == 0 or not values:
        return -1
    if not node1 or not node2:
        return -1
    root = buildBST(values, node1, node2)
    if root is None:
        return -1
    commonNode = lowestCommonAncestor(root, node1, node2)
    dist = getDistance(commonNode, node1) + getDistance(commonNode, node2)
    return dist


def getDistance(startNode, destVal):
    if not startNode:
        return 0
    if startNode.val == destVal:
        return 0
    node = startNode.left
    if startNode.val < destVal:
        node = startNode.right
    return 1 + getDistance(node, destVal)


def lowestCommonAncestor(root, node1, node2):
    while True:
        if root.val > node1 and root.val > node2:
            root = root.left
        elif root.val < node1 and root.val < node2:
            root = root.right
        else:
            return root


def buildBST(values, node1, node2):
    root = None
    nodeStatus1 = False
    nodeStatus2 = False
    for val in values:
        if val == node1:
            nodeStatus1 = True
        if val == node2:
            nodeStatus2 = True
        node = TreeNode(val)
        if root is None:
            root = node
            continue
        addToBSTree(root, node)
    if not nodeStatus1 or not nodeStatus2:
        return None
    return root


def addToBSTree(root, node):
    curr = root
    if curr.val > node.val:
        if curr.left is None:
            curr.left = node
        else:
            curr = curr.left
    else:
        if curr.right is None:
            curr.right = node
        else:
            curr = curr.right

if __name__ == '__main__':
    num = 6
    values = [5,6,3,4,1,2]
    values = [8,5,1,7,10,12]
    node1 = 7
    node2 = 10
    x = bstDistance(num, values, node1, node2)
    print(x)


"""
def insert(root, val):
    if root == None:
        return TreeNode(val=val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

bst = []
def preorder(root):
    if root == None:
        bst.append(None)
        return
    bst.append(root.val)
    preorder(root.left)
    preorder(root.right)

def lowestCommonAncestor(root, p, q):
    # :type root: TreeNode
    # :type p: int
    # :type q: int
    # :rtype: TreeNode
    parent_val = root.val

    if p < parent_val and q < parent_val:
        return lowestCommonAncestor(root.left, p, q)

    if p > parent_val and q > parent_val:
        return lowestCommonAncestor(root.right, p, q)

    return root
        
def height(root, val):
    if root.val == val:
        return 0
    
    if val < root.val:
        return (height(root.left, val) + 1)
    else:
        return (height(root.right, val) + 1)

l = [4, 2, 7, 1, 3, 5]
p = 1
q = 2
root = None
for val in l:
    root = insert(root, val)
preorder(root)

print bst
lca = lowestCommonAncestor(root, p, q)
print lca.val
h1 = height(lca, p)
h2 = height(lca, q)
print h1, h2
print h1 + h2
"""


"""
Python Solution -- create BST from level-order traversal + Find LCA + add(Dist(LCA,node1), Dist(LCA,node2)
nums = [8,5,10,1,7,12]
node1 = 1
node2 = 10
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def findLCA(head,node1,node2):
    if node1 > node2:
        node1,node2 = node2,node1
    while head.val < node1 or head.val > node2:
        if head.val > node2:
            head = head.left
        if head.val < node1:
            head = head.right
    return head

def dist(lca,node):
    dist = 0
    while lca:
        if lca.val == node:
            return dist
        elif lca.val < node:
            lca = lca.right
        else:
            lca = lca.left
        dist += 1
    return -1

def LevelOrder(root,data):
    if root is None:
        root = TreeNode(data)
        return root
    if root.val < data:
        root.right = LevelOrder(root.right,data)
    else:
        root.left = LevelOrder(root.left,data)
    return root

def constructBST(nums,node1,node2):
    root = None
    for i in range(len(nums)):
        root = LevelOrder(root,nums[i])
    lca = findLCA(root,node1,node2)
    left_dist = dist(lca,node1)
    right_dist = dist(lca,node2)
    return left_dist + right_dist

print(constructBST(nums,node1,node2))
"""