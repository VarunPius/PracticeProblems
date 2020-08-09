# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    def verticalOrder(self, root):
        return


"""
def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = collections.deque([(root, 0)])
    while queue:
        node, i = queue.popleft()
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    i = 0
    while i < len(queue):
        node, x = queue[i]
        i += 1
        if node:
            cols[x].append(node.val)
            queue += (node.left, x - 1), (node.right, x + 1)
    return [cols[x] for x in sorted(cols)]

Thanks for sharing as always~! Instead of sorting, we can allocate results with the len of the map, since there is no gap. Please see the last block of my code.

class Solution:
    def verticalOrder(self, root):
        # :type root: TreeNode
        # :rtype: List[List[int]]
        if root == None:
            return []
        colMap = {}
        level = [(root, 0)]
        while level:
            newLevel = []
            for node, col in level:
                if col not in colMap:
                    colMap[col] = []
                colMap[col].append(node.val)
                if node.left:
                    newLevel.append((node.left, col-1))
                if node.right:
                    newLevel.append((node.right, col+1))
            level = newLevel
        
        res = [0] * len(colMap)
        offset = -min(colMap.keys())
        for k, l in colMap.items():
            res[k+offset] = l
        return res

"""

"""
Another solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def verticalOrder(self, root):
        
        # :type root: TreeNode
        # :rtype: List[List[int]]
        # 
        # this problem seemed very hard but actually once you draw a picture on a paper or in your brain, it becomes pretty clear.
        # - for the left  node, you set its index as index - 1
        # - for the right node, you set its index as index + 1
        # - use queue to loop through all the nodes in a tree
        # - set index as a key to the hashmap() and value as a list of vals
        # - add node.data into hashmap() with index as a key
        # - keep track of min and max index and store into solution list and return it
        
        if not(root): return []
        
        res, MIN, MAX = [], 0, 0
        table = {}
        queue = [(root,0)]
        
        while queue:
            
            # order matters
            node, index = queue.pop(0)
            if index not in table:
                table[index] = [node.val]
            else:
                table[index].append(node.val)
            
            # left comes first.
            if node.left:
                MIN = min(MIN, index - 1)
                queue.append((node.left, index - 1))
            if node.right:
                MAX = max(MAX, index + 1)
                queue.append((node.right, index + 1))
        
        for i in range(MIN,MAX+1):
            res.append(table[i])
        
        return res"""
