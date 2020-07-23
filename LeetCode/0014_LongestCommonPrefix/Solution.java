public class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder result = new StringBuilder();
        
        if (strs != null && strs.length > 0){
            Arrays.sort(strs);
            
            char[] c1 = strs[0].toCharArray();
            char[] c2 = strs[strs.length-1].toCharArray();
            
            for (int i = 0; i<c1.length; i++){
                if(c2.length > i && c2[i]==c1[i]){
                    result.append(c1[i]);
                }
                else 
                    return result.toString();
            }
        }
        
        return result.toString();
    }
}