from collections import deque

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def printInorderRecursive(root):
    if root:
        printInorderRecursive(root.left)
        print(str(root.val) + " ")
        printInorderRecursive(root.right)

def printPreOrderRecursive(root):
    if root:
        print(str(root.val) + " ")
        printPreOrderRecursive(root.left)
        printPreOrderRecursive(root.right)

def printPostOrderRecursive(root):
    if root:
        printPostOrderRecursive(root.left)
        printPostOrderRecursive(root.right)
        print(str(root.val) + " ")

def printInorderIterative(root):
    current = root
    stack = []

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.val)
            current = current.right
        else:
            break

def printPreOrderIterative(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    while(len(stack)>0):
        current = stack.pop()
        print(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return

def printPostOrderIterative(root):
    lst = []
    stck = deque() # [] 1 <-> 2 <-> 3 

    if not root:
        return None

    stck.append(root)
    prev = None
    while stck:
        curr = stck[-1] # peek()

        if (prev is None) or (prev.left == curr) or (prev.right == curr):
            if curr.left:
                stck.append(curr.left)
            elif curr.right:
                stck.append(curr.right)
            else:
                stck.pop()
                lst.append(curr.val)
        elif curr.left == prev:
            if curr.right:
                stck.append(curr.right)
            else:
                stck.pop()
                lst.append(curr.val)
        elif curr.right == prev:
            stck.pop()
            lst.append(curr.val)
        
        prev = curr
    
    output = ""
    for val in lst:
        output += str(val) + " -> "
    print(output)
    return


def initNodes():
    root = Node(8)
    a = Node(4)
    b = Node(12)
    c = Node(2)
    d = Node(6)
    e = Node(10)
    f = Node(14)
    g = Node(1)
    h = Node(3)
    i = Node(5)
    j = Node(7)
    k = Node(9)
    l = Node(11)
    m = Node(13)
    n = Node(15)

    root.left = a
    root.right = b
    a.left  = c
    a.right = d
    b.left  = e
    b.right = f
    c.left  = g
    c.right = h
    d.left  = i
    d.right = j
    e.left  = k
    e.right = l
    f.left  = m
    f.right = n

    return root

def main():
    root = initNodes()
    print("Inorder Recursive Traversal")
    printInorderRecursive(root)
    print("Inorder Iterative Traversal")
    printInorderIterative(root)

    print("PreOrder Recursive Traversal")
    printPreOrderRecursive(root)
    print("PreOrder Iterative Traversal")
    printPreOrderIterative(root)

    print("PostOrder Recursive Traversal")
    printPostOrderRecursive(root)
    print("PostOrder Iterative Traversal")
    printPostOrderIterative(root)


if __name__ == '__main__':
    main()

"""
Tree:
                            8
              /-----------/   \---------\         
            4                             12
     /-----/ \-----\             /-------/  \---\
    2               6           10              14
  /   \           /   \        /   \          /    \ 
1       3       5       7     9     11      13       15
            
stack = 1 2 3 4 
list = 1, 3, 2, 5 7 6 4 9 11 ... 8

"""