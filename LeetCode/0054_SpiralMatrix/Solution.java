public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> op = new ArrayList<Integer>();

        if(matrix.length == 0){
            return op;
        }

        int rowStrt = 0;
        int colStrt = 0;
        int rowEnd = matrix.length-1;
        int colEnd = matrix[0].length-1;

        while(rowStrt<=rowEnd && colStrt <= colEnd){
            for(int i = colStrt; i <= colEnd; i++){
                op.add(matrix[rowStrt][i]);
            }
            rowStrt++;

            for(int j = rowStrt; j<=rowEnd; j++){
                op.add(matrix[j][colEnd]);
            }
            colEnd--;

            if(rowStrt<=rowEnd){
                for(int i = colEnd; i>=colStrt; i--){
                    op.add(matrix[rowEnd][i]);
                }
            }
            rowEnd--;

            if(colStrt<=colEnd){
                for(int j = rowEnd; j>=rowStrt; j--){
                    op.add(matrix[j][colStrt]);
                }
            }
            colStrt++;
        }
        return op;
    }
}
