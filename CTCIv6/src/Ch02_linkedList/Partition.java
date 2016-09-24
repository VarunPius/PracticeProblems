package Ch02_linkedList;

import java.io.*;

public class Partition {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter number: ");
		int n = Integer.parseInt(br.readLine());

		Node head = new Node(5);
		head.insertNode(2);
		head.insertNode(23);
		head.insertNode(4);
		head.insertNode(22);
		head.insertNode(7);
		head.insertNode(15);
		head.insertNode(22);
		head.insertNode(11);
		head.insertNode(19);
		head.insertNode(12);

		System.out.println("input from here");
		head.displayList();

		System.out.println("output from here");
		Node hd = partitionList(head, n);
		hd.displayList();
	}

	public static Node partitionList(Node c, int x){
		
		Node beforeStart = null;
		Node beforeEnd = null;
		Node afterStart = null;
		Node afterEnd = null;

		while( c != null ){
			Node tmp = c.next;
			c.next = null;
			if( c.data < x ){
				if (beforeEnd == null){
					beforeStart = c;
					beforeEnd = c; 
				}
				else{
					beforeEnd.next = c;
					beforeEnd = beforeEnd.next;
				}
				c = tmp;
			}
			else {
				if(afterEnd == null){
					afterStart = c;
					afterEnd = afterStart;
				}
				else{
					afterEnd.next = c;
					afterEnd = afterEnd.next;
				}
				c = tmp;
			}
		}

		if (beforeEnd == null)
			return afterStart;
		else {
			beforeEnd.next = afterStart;
			return beforeStart;
		} 
	}
}

/*
public static LinkedListNode partition(LinkedListNode node, int x) {
	LinkedListNode head = node;
	LinkedListNode tail = node;
	
	// Partition list 
	while (node != null) {
		LinkedListNode next = node.next;
		if (node.data < x) {
			// Insert node at head. 
			node.next = head;
			head = node;
		} else {
			// Insert node at tail. 
			tail.next = node;
			tail = node;
		}	
		node = next;
	}
	tail.next = null;
	
	return head;
}
*/


