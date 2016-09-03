public class Solution {
    public int reverse(int x) {
        int result = 0;
        int tmpresult;
        while(x != 0){
            int tail = x%10;
            tmpresult = result*10 + tail;
            if ((tmpresult-tail)/10 != result)
                return 0; // for overflow
            result = tmpresult;
            x = x/10;
        }
        return result;
    }
}