__author__ = 'VarunPius'


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def setNext(self, next_node):
        self.next = next_node

    def hasNext(self):
        return self.next is not None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def insert_at_end(self, next_node):
        tmp_node = self

        if(tmp_node):
            while tmp_node.hasNext():       #tmp_node.next can also b used
                tmp_node = tmp_node.getNext()

        tmp_node.setNext(next_node)


    def printList(self):
        tmp_node = self

        printList = []

        if (tmp_node):
            while tmp_node:
                printList.append(str(tmp_node.getData())) #instead of tmp_node.getData() we can use tmp_node.data
                tmp_node = tmp_node.getNext()  #instead of tmp_node.getNext() we can use tmp_node.next

        op = ''
        for data in printList:
            op = op + data + '->'

        op = op[:-2]
        print(op)


def main():
    hd = Node(5)

    hd.insert_at_end(Node(9))
    hd.insert_at_end(Node(10))
    hd.insert_at_end(Node(4))

    hd.printList()

if __name__ == '__main__':
    main()
