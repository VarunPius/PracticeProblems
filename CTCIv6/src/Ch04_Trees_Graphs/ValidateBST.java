package Ch04_Trees_Graphs;

public class ValidateBST {
	public static void main(String[] args) {
		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8};
		TreeNode root = TreeNode.createBST(nos);

		boolean op1 = checkIfBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
		System.out.println(op1);
		
		int[] nos2 = {1, 5, 2, 4, 3, 6, 14, 8};
		TreeNode root2 = TreeNode.createBST(nos2);
		
		boolean op2 = checkIfBST(root2, Integer.MIN_VALUE, Integer.MAX_VALUE);
		System.out.println(op2);
		
	}

	public static boolean checkIfBST(TreeNode node, int min, int max){
		if(node == null)
			return true;

		if((node.data <= min)||(node.data > max))
			return false;

		if(!checkIfBST(node.left, min, node.data)||!checkIfBST(node.right, node.data, max))
			return false;

		return true;
	}
}
