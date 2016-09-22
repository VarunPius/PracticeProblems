import java.io.*;
import java.util.*;

public class CheckPermutation {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		//Sort and compare is easier approach
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter String 1: ");
		String str1 = br.readLine();
		System.out.println("Enter String 2: ");
		String str2 = br.readLine();
		
		boolean op = checkPerm(str1, str2);
		System.out.println(op);
	}
	
	public static boolean checkPerm(String s1, String s2){
		if (s1.length() != s2.length())
			return false;
		
		HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
		char[] c1 = s1.toCharArray();
		char[] c2 = s2.toCharArray();
		
		for (int i = 0; i< c1.length; i++){
			if(hm.containsKey(c1[i]))
				hm.put(c1[i], hm.get(c1[i]) + 1);
			else
				hm.put(c1[i], 1);			
		}
			
		for (int i = 0; i< c2.length; i++){
			if(hm.containsKey(c2[i]) )
				hm.put(c2[i], hm.get(c2[i]) - 1);
			else 
				return false;
		}
		
		/*if(hm.containsValue(0))
			return false;
*/		
		int flag=0;
		for(Integer value:hm.values()){
			if(value!=0){
				flag=1;
				break;
			}
		}
		if(flag==0){
			return true;
			//System.out.println("Permutation");
		}
		else{
			return false;
			//System.out.println("Not Permutation");
		}
	}

}
