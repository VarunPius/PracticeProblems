package Ch04_Trees_Graphs;

public class Successor {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8};
		TreeNode root = TreeNode.createBST(nos);

		TreeNode succ = inOrderSucc(root.right.right);
		
		if(succ != null)
			System.out.println(succ.data);
		else
			System.out.println("Empty... No successor");
	}

	public static TreeNode inOrderSucc(TreeNode root){
		if(root == null)
			return null;

		if(root.parent == null || root.right != null){
			return leftChild(root.right);
		}
		else{
			TreeNode q = root;
			TreeNode x = root.parent;

			while(x != null && q != x.left){
				q = x;
				x = x.parent;
			}

			return x;
		}
	}

	public static TreeNode leftChild(TreeNode node){
		if(node == null)
			return null;

		while(node.left != null){
			node = node.left;
		}

		return node;
	}

}
