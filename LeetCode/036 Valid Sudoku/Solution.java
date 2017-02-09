public class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set seen = new HashSet();
        
        for(int i = 0; i<9; i++){
            for(int j = 0; j<9; j++){
                if(board[i][j] != '.'){
                    char num = board[i][j];
                    
                    if(!seen.add(num + " Row: " + i) ||
                       !seen.add(num + " Column: " + j)||
                       !seen.add(num + " Block: " + i/3 +"-"+j/3))
                       return false;
                }
            }
        }
        return true;
    }
}