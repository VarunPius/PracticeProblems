public class Solution {
    public void rotate(int[][] matrix) {
        int len = matrix.length;
        for(int r = 0; r<len/2 ; r++){
            int[] tmp = matrix[r];
            matrix[r] = matrix[len-1-r];
            matrix[len-1-r] = tmp;
        }

        for(int r = 0; r<len ; r++){
            for(int c = r; c<matrix[r].length; c++){
                int tmp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = tmp;
            }
        }
    }
}
