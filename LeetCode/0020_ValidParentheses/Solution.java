public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<Character>();
        
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == ')'){
                if(stk.size() != 0 && stk.peek() == '('){
                    stk.pop();
                    continue;
                }
                else
                    return false;
            }
            
            if(s.charAt(i) == ']'){
                if(stk.size() != 0 && stk.peek() == '['){
                    stk.pop();
                    continue;
                }
                else
                    return false;
            }

            if(s.charAt(i) == '}'){
                if(stk.size() != 0 && stk.peek() == '{'){
                    stk.pop();
                    continue;
                }
                else
                    return false;
            }
            stk.push(s.charAt(i));
        }
        
        if (stk.size() == 0)
            return true;
        return false;
    }
}