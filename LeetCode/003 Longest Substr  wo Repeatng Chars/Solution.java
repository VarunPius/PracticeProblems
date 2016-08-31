public class Solution {
    public int lengthOfLongestSubstring(String s) {
    	if (s == null || s.length() == 0)
    		return 0;

        int i = 0;
        int currMax = 0;
        int strArray[] = new int[256];
        Arrays.fill(strArray, -1);
        
        for (int j = 0; j<s.length(); j++){
        	if(strArray[s.charAt(j)]>=i){
        		i = strArray[s.charAt(j)] + 1;
        	}

        	strArray[s.charAt(j)] = j;
        	currMax = Math.max(currMax, j-i+1);
        }
        return currMax;

    }
}

//My original solution not accepted due to time exceed:
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        int currMax = 0;
        HashMap<Character, Integer> mp = new HashMap<Character, Integer>();
        
        for (int i = 0; i < len; i++){
            if(!mp.containsKey(s.charAt(i))){
                mp.put(s.charAt(i), i);
            }
            else{
                currMax = Math.max(currMax, mp.size());
                i = mp.get(s.charAt(i));
                mp.clear();
            }
        }
        
        return Math.max(currMax, mp.size()); ;
    }
}



// Here is a solution for O(n) runtime and O(n) space complexities

public int lengthOfLongestSubstring(String s) {
        
        if (s == null || s.length() == 0) return 0; 
        
        int len = s.length();
        if (len == 1) return 1; 
        
        HashSet<Character> set = new HashSet<Character>();
        int i, j = 0, maxLen = 0;
        
        for ( i = 0; i < len; i++ ) {
            
            char currentChar = s.charAt(i);
            
            if ( set.contains(currentChar) ) {
                
                maxLen = Math.max(maxLen, i-j);
                
                while ( s.charAt(j) != s.charAt(i) ) 
                    set.remove(s.charAt(j++)); 
                
                j++;
                
            } else { 
                set.add(currentChar);
            }
        }
        
        maxLen = Math.max(maxLen, i-j);
        return maxLen;
            
    }
