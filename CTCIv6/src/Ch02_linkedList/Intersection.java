package Ch02_linkedList;

public class Intersection {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Node head1 = new Node(5);
		head1.insertNode(6);
		head1.insertNode(7);
		head1.insertNode(8);

		Node head2 = new Node(9);
		head2.insertNode(10);

		Node c = new Node(12);
		Node d = new Node(13);
		Node e = new Node(14);
		c.next = d;
		d.next = e;

		head1.next.next.next.next = c;
		head2.next.next = c;

		System.out.println("List1:");
		head1.displayList();
		System.out.println();
		System.out.println("List2:");
		head2.displayList();

		Node cmn = intersectNode(head1, head2);

		System.out.println();
		System.out.println("commonNode: " + cmn.data);

	}

	public static Node intersectNode(Node l1, Node l2){
		Node tmp1 = l1;
		Node tmp2 = l2;
		Result l1Rslt = linkedListLen(tmp1);
		Result l2Rslt = linkedListLen(tmp2);

		if(l1Rslt.nd != l2Rslt.nd)
			return null;
		
		Node cmn;
		if(l1Rslt.len > l2Rslt.len){
			Node strt1 = freePass(l1, l1Rslt.len - l2Rslt.len);

			cmn = commonNode(strt1, l2);
		}
		else if (l1Rslt.len < l2Rslt.len){
			Node strt2 = freePass(l2, l2Rslt.len - l1Rslt.len);

			cmn = commonNode(l1, strt2);
		}
		else{
			cmn = commonNode(l1, l2);
		}

		return cmn;
	}

	public static Result linkedListLen(Node l1){
		int len = 1;

		while (l1.next != null){
			len++;
			l1 = l1.next;
		}
		
		return new Result(len, l1);
	} 

	public static Node commonNode(Node l1, Node l2){
		while(l1 != l2 && l1 != null && l2 != null){
			l1 = l1.next;
			l2 = l2.next;
		}

		return l1;
	}

	public static Node freePass(Node ll, int n){
		while (n > 0){
			ll = ll.next;
			n--;
		}
		return ll;
	}

}

class Result{
	int len;
	Node nd;

	Result(int len, Node nd){
		this.len = len;
		this.nd = nd;
	}
}

