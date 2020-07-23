public class Solution {
    public int myAtoi(String str) {
        int count = 0;
        double rslt = 0;
        int sign = 1;
        char[] nosArray = str.toCharArray();

        for(char c: nosArray){
            count++;

            if (c>='0' && c<='9'){
                rslt = rslt*10 + (c-'0');
                //count--;
            }
            else if (c == '-' && count == 1){
                sign = -1;
            }
            else if (c == '+' && count == 1){
                sign = 1;
            }
            else if (c == ' ' && count == 1){
                count--;
            }
            else
                break;
        }

        if (rslt > Integer.MAX_VALUE){
            if(sign == 1)
                return Integer.MAX_VALUE;
            else
                return Integer.MIN_VALUE;

        }
        else
            return (int)rslt*sign;
    }
}
