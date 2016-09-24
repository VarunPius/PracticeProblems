package Ch02_linkedList;

public class DeleteMiddleNode {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Node head = new Node(5);
		head.insertNode(2);
		
		//Node c = new Node(7);
		head.insertNode(7);
		
		head.insertNode(23);
		head.insertNode(4);
		head.insertNode(23);
		Node c = head.next.next.next;
		System.out.println("input from here");
		head.displayList();

		deleteMid(c);
		System.out.println("Output from here");
		head.displayList();
	}
	
	public static void deleteMid(Node c){
		if(c.next != null){
			c.data = c.next.data;
			c.next = c.next.next;			
		}
	}

}
