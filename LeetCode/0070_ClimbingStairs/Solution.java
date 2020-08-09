public class Solution {
    public int climbStairs(int n) {
        int c1 = 0, c2 = 1;
        for(int i = 1; i <= n; i++){
        	int tmp = c1+c2;
        	c1 = c2;
        	c2 = tmp;
        }

        return c2;
    }
}
