public class Solution {
    public String simplifyPath(String path) {
        Deque<String> stck = new LinkedList<>();
        Set<String> st = new HashSet<String>(Arrays.asList("..", ".", ""));

        //String[] dir = path.split("/");

        for(String tkn: path.split("/")){
        	if(tkn.equals("..") && !stck.isEmpty()){   //Mistake: tkn == ".." didn't work because it ispointing to the reference of ..
        		stck.pop();
        	}
        	else if (!st.contains(tkn)){
        		stck.push(tkn);
        	}
        }

        String res= "";

        for(String tkn:stck){
        	res = "/" + tkn + res;
        }

        if(res == "")
            res = "/";

        return res;
    }
}
