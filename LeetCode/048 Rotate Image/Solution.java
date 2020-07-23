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

/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/