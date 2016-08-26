__author__ = 'VarunPius'


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def setNext(self, next_node):
        self.next = next_node

    def hasNext(self):
        return self.next is None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data


class LinkedListFunc:
    ##Node head
    def __init__(self):
        self.first = Node(2)

    def insert_at_end(self, next_node):
        tmp_node = self.first

        if (tmp_node):
            while tmp_node.hasNext():
                tmp_node = tmp_node.getNext()

        tmp_node.setNext(Node(next_node))

    def printList(self):
        tmp_node = self.first

        if (tmp_node):
            while tmp_node.hasNext():
                print(tmp_node.getData() + " -> ")
                tmp_node.getNext()
        tmp_node.getData()



hd = Node(5)
ll = LinkedListFunc()

ll.insert_at_end(hd)
ll.insert_at_end(Node(9))
ll.insert_at_end(Node(10))
ll.insert_at_end(Node(4))

ll.printList()









