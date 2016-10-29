package Ch02_linkedList;

import java.util.*;

public class Palindrome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Node head = new Node(5);
		head.insertNode(6);
		head.insertNode(7);
		//head.insertNode(7);
		head.insertNode(6);
		head.insertNode(5);

		boolean op = isPalindrome(head);

		System.out.println("Output: " + op);

	}

	public static boolean isPalindrome(Node head){
		Node slow = head;
		Node fast = head;

		Stack<Integer> st = new Stack<Integer>();

		while(fast != null && fast.next != null){
			st.push(slow.data);
			slow = slow.next;
			fast = fast.next.next;
		}

		if(fast != null){
			slow = slow.next;
		}

		while(slow != null){
			if(st.pop() != slow.data){
				return false;
			}
			slow = slow.next;
		}

		return true;
	}
}
