public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[] path = new int[m];
        path[0] = grid[0][0];

		for(int i = 1; i<m; i++){
			path[i] = path[i-1] + grid[i][0];
		}

        for(int j = 1; j<n; j++){
        	for(int i = 0; i<m; i++){
        		if(i!=0 && j!=0){
        			path[i] = grid[i][j] + Math.min(path[i-1], path[i]);
        		}
        		else{
        			path[i]+=grid[i][j];
        		}
        	}
        }

        return path[m-1];
    }
}
