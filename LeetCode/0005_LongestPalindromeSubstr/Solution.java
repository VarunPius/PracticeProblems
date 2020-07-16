public class Solution {
    int frst, currMax;
    
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len<2){
            return s;
        }
        
        for (int i = 0; i<len;i++){
            palindromeHelper(s, i, i);
            palindromeHelper(s, i, i+1);
        }
        return s.substring(frst, frst+currMax);
    }
    
    public void palindromeHelper(String s, int j, int k){
        while (j>= 0 && k<s.length() && s.charAt(j)==s.charAt(k)){
            j--;
            k++;
        }
        if (currMax < k-j-1){
            frst = j+1;
            currMax = k-j-1;
        }
    }
}