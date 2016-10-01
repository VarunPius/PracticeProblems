package BinaryTree;

public class BinaryTree {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Node root = new Node(8);
		Node a = new Node(4);
		Node b = new Node(12);
		Node c = new Node(2);
		Node d = new Node(6);
		Node e = new Node(10);
		Node f = new Node(14);
		Node g = new Node(1);
		Node h = new Node(3);
		Node i = new Node(5);
		Node j = new Node(7);
		Node k = new Node(9);
		Node l = new Node(11);
		Node m = new Node(13);
		Node n = new Node(15);

		root.left = a;
		root.right = b;
		a.left  = c;
		a.right = d;
		b.left  = e;
		b.right = f;
		c.left  = g;
		c.right = h;
		d.left  = i;
		d.right = j;
		e.left  = k;
		e.right = l;
		f.left  = m;
		f.right = n;

		BinaryTree bt = new BinaryTree();

		System.out.println("Inorder Traversal: ");
		bt.inOrder(root);

		System.out.println("Pre order Traversal: ");
		bt.preOrder(root);

		System.out.println("Post order Traversal: ");
		bt.postOrder(root);
  }

	public void preOrder(Node nd){
		//Node tmp = nd;
		if(nd != null){
			System.out.println("Node value is: " + nd.value);
			preOrder(nd.left);
			preOrder(nd.right);
		}
	}

	public void inOrder(Node nd){
		if(nd != null){
			inOrder(nd.left);
			System.out.println("Node value is: " + nd.value);
			inOrder(nd.right);
		}
	}

	public void postOrder(Node nd){
		if(nd != null){
			postOrder(nd.left);
			postOrder(nd.right);
			System.out.println("Node value is: " + nd.value);
		}
	}

}

/*
Inorder Traversal:
Node value is: 4
Node value is: 2
Node value is: 1
Node value is: 3
Node value is: 6
Node value is: 5
Node value is: 7
Node value is: 8
Node value is: 12
Node value is: 10
Node value is: 9
Node value is: 11
Node value is: 14
Node value is: 13
Node value is: 15
Pre order Traversal:
Node value is: 8
Node value is: 4
Node value is: 2
Node value is: 1
Node value is: 3
Node value is: 6
Node value is: 5
Node value is: 7
Node value is: 12
Node value is: 10
Node value is: 9
Node value is: 11
Node value is: 14
Node value is: 13
Node value is: 15
Post order Traversal:
Node value is: 4
Node value is: 2
Node value is: 1
Node value is: 3
Node value is: 6
Node value is: 5
Node value is: 7
Node value is: 12
Node value is: 10
Node value is: 9
Node value is: 11
Node value is: 14
Node value is: 13
Node value is: 15
Node value is: 8


*/
