public class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){return false;}
        int med = x;
        int rslt = 0;
        while(med!=0){
            int tmp = med%10;
            rslt = rslt*10 + tmp;
            med=med/10;
        }
        
        if (rslt == x){
            return true;
        }
        return false;
    }
}