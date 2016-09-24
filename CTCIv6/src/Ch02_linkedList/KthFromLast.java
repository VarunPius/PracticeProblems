package Ch02_linkedList;

import java.io.*;

public class KthFromLast {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter number: ");
		int n = Integer.parseInt(br.readLine());

		Node head = new Node(5);
		head.insertNode(2);
		head.insertNode(23);
		head.insertNode(4);
		head.insertNode(23);
		head.insertNode(45);
		head.insertNode(6);
		head.insertNode(89);
		System.out.println("Input from here");
		head.displayList();

		kthlast(n, head);
	}
	
	public static void kthlast(int cnt, Node head){
		Node frnt = head;
		Node curr = head;
		
		int n = cnt;
		
		while(n != 0 && curr != null){
			curr = curr.next;
			n--;
		}
		
		while(curr != null){
			frnt = frnt.next;
			curr = curr.next;
		}
		
		System.out.println("Output from here:");
		System.out.println(frnt.data);
	}

}
