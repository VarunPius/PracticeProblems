package Ch02_linkedList;

public class LoopDetection {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Node head = new Node(5);
		head.insertNode(6);
		head.insertNode(7);

		Node a = new Node(10);
		Node b = new Node(11);
		Node c = new Node(12);
		Node d = new Node(13);
		Node e = new Node(14);
		Node f = new Node(15);
		
		head.next.next.next = a;
		a.next = b;
		b.next = c;
		c.next = d;
		d.next = e;
		e.next = f;
		f.next = a;
		b.next = c;
		c.next = d;
		d.next = e;
		e.next = f;
		f.next = a;

		Node cmn = loopHelper(head);
		
		System.out.println("Common node is: " + cmn.data);
	}
	
	public static Node loopHelper(Node ll){
		Node slow = ll;
		Node fast = ll;
		
		while(fast != null && fast.next != null){
			slow = slow.next;
			fast = fast.next.next;
			if (slow == fast){
				break;
			}
		}
		
		if(fast == null || fast.next == null)
			return null;
		
		slow = ll;
		while(slow != fast){
			slow = slow.next;
			fast = fast.next;
		}
		
		return fast;
	}

}
