package Ch02_linkedList;

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
		head.displayList();

		//Node del = deleteDups(head);
		Node delwo = delWoBuffer(head);

		System.out.println("Output from here");
		delwo.displayList();
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

			while (recur.next != null){
				if(recur.next.data == curr.data)
					recur.next = recur.next.next;
				else
					recur = recur.next;
			}

			curr = curr.next;
		}

		return head;
	}
}
