package Ch04_Trees_Graphs.minimal_tree;

public class TreeNode {
  TreeNode left;
  TreeNode right;
  TreeNode parent;
  int data;
  int size;

  public TreeNode(int d){
    data = d;
    size = 1;
  }

  public static TreeNode createBST(int[] arr){
    return createBST(arr, 0, arr.length - 1);
  }

  private static TreeNode createBST(int[] arr, int start, int end){
    if (end < start)
      return null;

    int mid = (start + end)/2;

    TreeNode rt = new TreeNode(arr[mid]);

    rt.setLeft(createBST(arr, start, mid -1));
    rt.setRight(createBST(arr, mid+1, end));

    return rt;
  }

  public void setLeft(TreeNode left){
    this.left = left;

    if(left != null){
      left.parent = this;
    }
  }

  public void setRight(TreeNode right){
    this.right = right;

    if(right != null){
      right.parent = this;
    }
  }

  public int height(){
    int leftHt = left!=null?left.height():0;
    int rightHt = right!=null?right.height():0;

    return 1 + Math.max(leftHt, rightHt);
  }

  public boolean isBST(){
    if(left != null){
      if(data < left.data || left.isBST()){
        return false;
      }
    }

    if(right != null){
      if(data>=right.data || right.isBST()){
        return false;
      }
    }

    return true;
  }
}
