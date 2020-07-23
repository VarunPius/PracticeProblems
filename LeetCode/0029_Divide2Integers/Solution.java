public class Solution {
    public int divide(int dividend, int divisor) {
        long l_dividend = (long) dividend;
        long l_divisor = (long) divisor;

        int sign = 1;

        if (l_dividend < 0){
        	l_dividend = -l_dividend;
        	sign = -sign;
        }

        if (l_divisor < 0){
        	l_divisor = -l_divisor;
        	sign = -sign;
        }

        long quo = quotient(l_dividend, l_divisor);

        quo = quo*sign;

        if (quo > Integer.MAX_VALUE)
        	return Integer.MAX_VALUE;
        else if (quo < Integer.MIN_VALUE)
        	return Integer.MIN_VALUE;

        return (int)quo;

    }

    public long quotient(long dividend, long divisor){
    	long cnt = 1;
    	long orig = divisor;

    	while(divisor<<1 < dividend){
    		divisor <<=1;
    		cnt<<=1;
    	}

    	if (divisor == dividend){
    		return cnt;
    	}
    	else {
    		cnt = cnt + quotient(dividend - divisor, divisor);
    	}

    	return cnt;
    }
}