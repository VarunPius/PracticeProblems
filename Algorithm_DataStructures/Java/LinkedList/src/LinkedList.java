/**
 * Created by VarunPius on 12/28/2015.
 */

class Node{
    int data;
    Node next;

    Node(int data)
    {
        this.data = data;
    }
}

class LinkedListFunc
{
    Node head;

    public void insertAtEnd(Node n)
    {
        if (head == null)
        {
            head = n;
        }
        else
        {
            Node tmp = head;
            while (tmp.next != null)
                tmp = tmp.next;

            tmp.next = n;
        }

    }

    public void printLinkedList(Node head)
    {
        Node tmp = head;

        while (tmp != null)
        {
            System.out.print(tmp.data + " -> ");
            tmp = tmp.next;
        }
    }

    public void reverseLinkedList(Node head)
    {
        Node curr = head;
        Node previousNode = null;
        Node nextNode = null;

        Node tmp = previousNode;
        nextNode = previousNode;
        curr.next = previousNode;
        nextNode.next = curr;
        nextNode.next.next = previousNode;

    }
}
public class LinkedList {
    public static void main(String[] args)
    {
        Node head = new Node(10);

        LinkedListFunc list = new LinkedListFunc();

        list.insertAtEnd(head);
        list.insertAtEnd(new Node(4));
        list.insertAtEnd(new Node(3));
        list.insertAtEnd(new Node(9));
        Node tail = new Node(11);
        list.insertAtEnd(tail);

        list.printLinkedList(head);
        System.out.println();
        list.printLinkedList(tail);
    }
}

class reverseLinkedList
{

}
