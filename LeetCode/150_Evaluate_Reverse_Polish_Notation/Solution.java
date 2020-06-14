class Solution {
    public int evalRPN(String[] tokens) {
        int returnValue = 0;
        String tokenSet = "+-/*";

        Deque<Integer> stck = new LinkedList<>();
        
        for (String token : tokens){
            if(!tokenSet.contains(token)){
                stck.push(Integer.parseInt(token));
            }
            else{
                int num1 = stck.pop();
                int num2 = stck.pop();
                switch(token){
                    case "+":
                    stck.push(num1 + num2);
                    break;
                    case "-":
                    stck.push(num2 - num1);
                    break;
                    case "/":
                    stck.push((int)(num2 / num1));
                    break;
                    case "*":
                    stck.push(num2 * num1);
                    break;
                }
            }
        }
        returnValue = stck.pop();
        return returnValue;
        
    }
}