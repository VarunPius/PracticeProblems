package Ch04_Trees_Graphs;

public class PathsWithSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
		TreeNode root = TreeNode.createBST(nos);

		int op = countPaths(root, 7);

		System.out.println(op);
		//Output: 2
	}

	public static int countPaths(TreeNode node, int target){
		if (node == null)
			return 0;

		int pathNode = countPaths(node, target, 0);
		int pathLeft = countPaths(node.left, target);
		int pathRight = countPaths(node.right, target);

		return pathNode + pathLeft + pathRight;
	}

	public static int countPaths(TreeNode node, int target, int aggSum){
		if(node == null)
			return 0;

		int pathCnt = 0;
		aggSum += node.data;

		if(aggSum == target){
			pathCnt++;
		}

		pathCnt += countPaths(node.left, target, aggSum);
		pathCnt += countPaths(node.right, target, aggSum);
		return pathCnt;
	}

}
