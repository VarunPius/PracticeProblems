public class Solution {
    public int lengthOfLastWord(String s) {
        int i = 0;
        if(s.isEmpty() || s.equals("")||s.equals(" "))
            return 0;

        if(s != " "){
            String[] s_arr = s.split(" ");
            if(s_arr.length > 0){
                String last = s_arr[s_arr.length - 1];
                i = last.length();
            }
        }

        return i;
    }
}

/*
Other soln:
public class Solution {
public int lengthOfLastWord(String s) {
int len = s.length();
int i = len -1;
int empty = 0;
if(s == null || len == 0)
return 0;
while(i>=0 && s.charAt(i)==' '){
i--;
empty++;
}
while(i>=0 && s.charAt(i)!=' ')
i--;
return len- empty - (i+1);
}
}
*/
