public class Solution {
    public int romanToInt(String s) {
        char[] ch = s.toCharArray();
        int sum = 0;
        
        for (int i = 0; i<ch.length; i++){
            int val = getValue(ch[i]);
            if((i+1)<ch.length && val < getValue(ch[i+1])){
                sum = sum - val;
            }
            else 
                sum = sum + val;
        }
        return sum;
    }
    
    public int getValue(char c){
        switch(c){
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
        }
        return 0;
    }
}