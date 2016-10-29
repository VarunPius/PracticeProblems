package Ch04_Trees_Graphs;

public class CommonAncestor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
		TreeNode root = TreeNode.createBST(nos);

		//Without using links to parents:
		TreeNode p = root.find(4);
		TreeNode q = root.find(6);
		//System.out.println(p.left.data);
		TreeNode anc1 = ancestorChk1(root, p, q);
		System.out.println(anc1.data);

		p = root.find(4);
		q = root.find(10);
		//System.out.println(p.left.data);
		TreeNode anc2 = ancestorChk1(root, p, q);
		System.out.println(anc2.data);

		p = root.find(13);
		q = root.find(15);
		//System.out.println(p.left.data);
		TreeNode anc3 = ancestorChk1(root, p, q);
		System.out.println(anc3.data);

		//Output: 4, 8, 14

		//Using links to parents:
		p = root.find(4);
		q = root.find(6);
		//System.out.println(p.left.data);
		TreeNode anc4 = ancestorChk2(root, p, q);
		System.out.println(anc1.data);

		p = root.find(4);
		q = root.find(10);
		//System.out.println(p.left.data);
		TreeNode anc5 = ancestorChk2(root, p, q);
		System.out.println(anc2.data);

		p = root.find(13);
		q = root.find(15);
		//System.out.println(p.left.data);
		TreeNode anc6 = ancestorChk2(root, p, q);
		System.out.println(anc3.data);
	}

	public static TreeNode ancestorChk1(TreeNode root, TreeNode p, TreeNode q){
		if(!covers(root, p)||!covers(root, q)){
			System.out.println("Nodes don't cover");
			return null;
		}

		return ancestorHelper(root, p, q);
	}

	public static TreeNode ancestorHelper(TreeNode root, TreeNode p, TreeNode q){
		if(root == null||root == p||root == q)
			return root;

		boolean pIsOnLeft = covers(root.left, p);
		boolean qIsOnLeft = covers(root.left, q);

		if(pIsOnLeft !=qIsOnLeft)
			return root;

		TreeNode childSide = pIsOnLeft?root.left:root.right;

		return ancestorHelper(childSide, p, q);
	}

	public static boolean covers(TreeNode nd1, TreeNode nd2){
		if(nd1 == null)
			return false;

		if(nd1 == nd2)
			return true;

		return covers(nd1.left, nd2)||covers(nd1.right, nd2);
	}

	public static TreeNode getSibling(TreeNode nd){
		if(nd == null || nd.parent == null)
			return null;

		TreeNode prnt = nd.parent;

		TreeNode sibling = prnt.left==nd?prnt.right:prnt.left;
		return sibling;
	}

	public static TreeNode ancestorChk2(TreeNode root, TreeNode p, TreeNode q){
		if(!covers(root, p)||!covers(root, q)){
			System.out.println("Nodes don't cover");
			return null;
		}
		else if(covers(p, q))
			return p;
		else if(covers(q,p))
			return q;

		TreeNode sibling = getSibling(p);
		TreeNode par = p.parent;

		while(!covers(sibling, q)){
			sibling = getSibling(par);
			par = par.parent;
		}

		return par;
	}

}
