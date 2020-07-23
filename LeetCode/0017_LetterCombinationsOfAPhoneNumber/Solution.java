public class Solution {
    public static final char[][] digNum = new char[][]{
        {' '},
        {},
        {'a', 'b', 'c'},
        {'d', 'e', 'f'},
        {'g', 'h', 'i'},
        {'j', 'k', 'l'},
        {'m', 'n', 'o'},
        {'p', 'q', 'r', 's'},
        {'t', 'u', 'v'},
        {'w', 'x', 'y', 'z'},
        {'*'},
        {'#'}
    };
    
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0){
            return Collections.emptyList();
        }
        
        List<String> rslt = new ArrayList<String>();
        letterHelper("", digits, rslt, 0);
        return rslt;
    }
    
    public void letterHelper(String prefix, String digits, List<String> rslt, int startIdx){
        if (prefix.length() == digits.length()){
            rslt.add(prefix);
            return;
        }
        
        //int val = Integer.parseInt(digits.charAt(startIdx)); char cannot be converted to string
        int val = getIntegerVal(digits, startIdx);
        for(int j = 0; j<digNum[val].length; j++){
            letterHelper(prefix + digNum[val][j], digits, rslt, startIdx + 1);
        }
    }
    
    public int getIntegerVal(String digits, int startIdx){
        char c = digits.charAt(startIdx);
        if (c == '*')
            return 10;
        else if (c == '#')
            return 11;
        else
            return Character.getNumericValue(c);
    }
}




