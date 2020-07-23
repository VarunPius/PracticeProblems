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
