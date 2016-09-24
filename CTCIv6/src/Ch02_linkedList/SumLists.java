package Ch02_linkedList;

public class SumLists {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Node head1 = new Node(5);
		head1.insertNode(2);
		head1.insertNode(9);
		System.out.println("List 1:");
		head1.displayList();

		System.out.println();

		Node head2 = new Node(6);
		head2.insertNode(2);
		head2.insertNode(1);
		System.out.println("List 2:");
		head2.displayList();
		
		System.out.println();
		System.out.println("Output:");
		Node sumHead = sumLst(head1, head2);

		sumHead.displayList();

	}
	
	public static Node sumLst(Node l1, Node l2){
		int carry = 0;
		Node first = new Node(0);
		Node curr = first;
		
		while(l1 != null || l2 != null || carry != 0){
			int value  = 0;
			value = value + carry;

			if(l1 != null ){
				value = value + l1.data;
				l1 = l1.next;
			}

			if(l2 != null){
				value = value + l2.data;
				l2 = l2.next;
			}

			carry = value/10;
			value = value%10;

			curr.next = new Node(value);
			curr = curr.next;
		}
		
		return first.next;

	}

}
