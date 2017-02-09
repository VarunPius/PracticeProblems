public class Solution {
    public int uniquePaths(int m, int n) {
        if(m == 0 || n == 0)
        	return 0;
        
        int[] path = new int[n];

        for(int i = 0; i<m; i++){
        	for(int j = 0; j<n; j++){
        		if(m==0||n==0)
        			path[j] = 1;
        		else{
        			path[j]+=path[j-1];
        		}
        	}
        }

        return path[n-1];
    }
}