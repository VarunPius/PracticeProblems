public class Solution {
    public String convert(String s, int numRows) {
        int len = s.length();
        
        StringBuffer[] sb = new StringBuffer[numRows];
        
        for (int j = 0; j<numRows; j++){
            sb[j] = new StringBuffer();
        }
        
        int i = 0;
        while(i<len){
            for (int idx = 0; idx < numRows && i<len; idx++){
                sb[idx].append(s.charAt(i++));
            }
            for (int idx = numRows-2; idx >= 1 && i<len; idx--){
                sb[idx].append(s.charAt(i++));
            }
        }
        
        for (int j = 1; j<numRows; j++){
            sb[0].append(sb[j]);
        }
        
        return sb[0].toString();
    }
}