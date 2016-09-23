package linkedList_02;

public class Node {
	int data;
	Node next;
	
	public Node(int d){
		data = d;
		next = null;
	}
	
	public void insertNode(int d){
		Node curr = this;
		
		while(curr != null && curr.next != null){
			curr = curr.next;
		}
		
		curr.next = new Node(d);
	}
	
	public void displayNode(){
		Node curr = this;
		
		while(curr != null){
			System.out.println(curr.data);
			curr = curr.next;
		}
	}
}
