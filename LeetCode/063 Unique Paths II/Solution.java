public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int width = obstacleGrid[0].length;

        int[] path = new int[width];

        path[0] = 1;

        for(int[] row:obstacleGrid){
        	for(int i = 0; i < width; i++){
        		if(row[i] == 1)
        			path[i] = 0;
        		else if (i>0)
        			path[i] += path[i-1];
        	}
        }

        return path[width - 1];
    }
}
