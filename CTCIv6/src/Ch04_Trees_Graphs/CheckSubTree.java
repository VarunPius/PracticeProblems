package Ch04_Trees_Graphs;

/*
Alternate approach is do a preorder traversal and forma String.
WHile forming string, substitute x for null.
This is because of following:

    3     4
   /       \
  4         3

Both the above trees have the same preorder traversal. So substituting x in place of nulls solves the issue.
*/

public class CheckSubTree {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[] array1 = {1, 2, 1, 3, 1, 1, 5};
		int[] array2 = {2, 3, 1};

		TreeNode t1 = TreeNode.createBST(array1);
		TreeNode t2 = TreeNode.createBST(array2);

		//System.out.println("Root of t1: " + t1.data);
		//System.out.println("Root of t2: " + t2.data);
		boolean op1 = checkTree(t1, t2);
		System.out.println(op1);

		int[] array3 = {1, 2, 3};
		TreeNode t3 = TreeNode.createBST(array3);
		//System.out.println("Root of t3: " + t3.data);
		//System.out.println("Root of t3.left: " + t3.left.data);
		//System.out.println("Root of t3.right: " + t3.right.data);
		boolean op2 = checkTree(t1, t3);
		System.out.println(op2);

		int[] array4 = {1, 2, 1};
		TreeNode t4 = TreeNode.createBST(array4);
		boolean op3 = checkTree(t1, t4);
		System.out.println(op3);

		//Output: false false true
	}

	public static boolean checkTree(TreeNode t1, TreeNode t2){
		if (t2==null)
			return true;

		return subtree(t1, t2);
	}

	public static boolean subtree(TreeNode t1, TreeNode t2){
		if(t1 == null)
			return false;

		if((t1.data == t2.data)&&matchTree(t1, t2))
			return true;

		return subtree(t1.left, t2)||subtree(t1.right, t2);
	}

	public static boolean matchTree(TreeNode t1, TreeNode t2){
		if((t1==null)&&(t2==null))
			return true;
		else if((t1==null)||(t2==null))
			return false;
		else if (t1.data != t2.data)
			return false;
		else return matchTree(t1.left, t2.left)&&matchTree(t1.right,t2.right);
	}
}
