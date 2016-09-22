public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> rslt = new ArrayList<String>();
        
        if (n == 0)
            return rslt;
        
        parenthesisRecursive("", n, n, rslt);
        
        return rslt;
    }
    
    public void parenthesisRecursive(String prefix, int left, int right, List<String> rslt){
        if (right == 0)
            rslt.add(prefix);
        
        if (left > 0)
            parenthesisRecursive(prefix + "(", left - 1, right, rslt);
        
        if (right > left)
            parenthesisRecursive(prefix + ")", left, right-1, rslt);
    }
}