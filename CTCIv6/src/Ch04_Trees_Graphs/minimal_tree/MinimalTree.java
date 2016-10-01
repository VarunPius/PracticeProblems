package Ch04_Trees_Graphs.minimal_tree;

public class MinimalTree {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8};

		TreeNode root = TreeNode.createBST(nos);
		System.out.println("Root: " + root.data);
		System.out.println("Created BST? " + root.isBST());
		System.out.println("Height: " + root.height());

	}

}
