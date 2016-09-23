package linkedList_02;

import java.util.*;

public class RemoveDups {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Node head = new Node(5);
		head.insertNode(2);
		head.insertNode(23);
		head.insertNode(4);
		head.insertNode(23);
		System.out.println("input from here");
		head.displayNode();
		
		Node del = deleteDups(head);
		
		System.out.println("Output from here");
		del.displayNode();		
		
	}
	
	public static Node deleteDups(Node head){
		Node curr = head;
		Node first = head;
		
		HashSet<Integer> hs = new HashSet<Integer>();
		
		hs.add(curr.data);
		//if(hs.contains(curr.data))
			//return curr.next;
		
		while(curr != null && curr.next != null){
			if(hs.contains(curr.next.data)){
				curr.next = curr.next.next;
			}
			else
				hs.add(curr.next.data);			
			curr = curr.next;			
		}
		
		return first;		
	}
	
	public static Node delWoBuffer(Node head){
		Node curr = head;
		//Node first = head;
		
		while (curr != null){
			Node recur = curr;
			
			while (recur != null){
				
			}
		}
			
		return head;
	}
}

