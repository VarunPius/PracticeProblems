package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Node head = new Node(5);
        head.addNext(7);
        head.addNext(8);
        head.addNext(9);
        System.out.println("Program ends here!");
        head.displayList();
    }
}

class Node{
    private int data;
    Node next = null;

    public Node(int d){
        this.data = d;
    }

    public void addNext(int d){
        Node new_Node = new Node(d);
        Node n = this;
        while (n.next != null){
            n = n.next;
        }
        n.next = new_Node;
    }

    public void displayList(){
        Node n = this;
        while(n != null && n.next != null){
            System.out.println("Value is:" + n.data + " and neighboring node value is: " + n.next.data);
            n = n.next;
        }

        System.out.println("Value is:" + n.data);
    }

    public Node deleteNode(Node head, int d){
        Node n = head;
        if ( n.data == d)
            return head.next;

        while(n.next != null){
            if(n.next.data == d){
                n.next = n.next.next;
                return head;
            }
            n = n.next;

        }
        return head;
    }
}