package Ch04_Trees_Graphs;

public class CheckBalanced {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8};
		TreeNode root = TreeNode.createBST(nos);

		int chk = chkHt(root);
		System.out.println("Output is: " + isBalanced(chk));
	}

	public static int chkHt(TreeNode root){
		if(root == null)
			return -1;

		int leftHt = chkHt(root.left);
		int rightHt = chkHt(root.right);

		if(Math.abs(leftHt - rightHt) > 1){
			return Integer.MIN_VALUE;
		}
		else{
			return Math.max(leftHt, rightHt) + 1;
		}
	}

	public static boolean isBalanced(int chkVal){
		if(chkVal == Integer.MIN_VALUE)
			return false;
		else
			return true;
	}

}
