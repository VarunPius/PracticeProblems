package Ch04_Trees_Graphs;

import java.util.*;

public class ListOfDepths {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[] nos = {1, 2, 3, 4, 5, 6, 7, 8};

		TreeNode root = TreeNode.createBST(nos);

		ArrayList<LinkedList<TreeNode>> rst = createList(root);
		printList(rst);
	}

	public static ArrayList<LinkedList<TreeNode>> createList(TreeNode root){
		ArrayList<LinkedList<TreeNode>> result = new ArrayList<LinkedList<TreeNode>>();

		LinkedList<TreeNode> curr = new LinkedList<TreeNode>();

		if(root != null){
			curr.add(root);
		}

		while(curr.size() != 0){
			result.add(curr);

			LinkedList<TreeNode> parents = curr;
			curr = new LinkedList<TreeNode>();

			for(TreeNode par : parents){
				if(par.left != null)
					curr.add(par.left);
				if(par.right != null)
					curr.add(par.right);
			}
		}

		return result;
	}

	public static void printList(ArrayList<LinkedList<TreeNode>> rslt){
		int depth = 0;
		for (LinkedList<TreeNode> lst : rslt){
			Iterator<TreeNode> i = lst.listIterator();

			System.out.println("The depth is: " + depth);
			while(i.hasNext()){
				TreeNode nd = i.next();
				System.out.println(nd.data);
			}
			System.out.println();
			depth++;
		}
	}
}

/*
The depth is: 0
4

The depth is: 1
2
6

The depth is: 2
1
3
5
7

The depth is: 3
8



*/
