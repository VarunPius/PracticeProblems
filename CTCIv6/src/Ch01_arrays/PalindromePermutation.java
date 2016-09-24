package Ch01_arrays;

import java.io.*;
import java.util.HashMap;

public class PalindromePermutation {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter String: ");
		String str = br.readLine();
		
		boolean op = palinPerm(str);
		
		System.out.println(op);

	}
	
	public static boolean palinPerm(String str){
		HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
		char[] c1 = str.toCharArray();

		for (int i = 0; i< c1.length; i++){
			if(hm.containsKey(c1[i]))
				hm.put(c1[i], hm.get(c1[i]) + 1);
			else if(c1[i] != ' ')
				hm.put(c1[i], 1);			
		}
		
		int oddCnt = 0;
		for(Integer value:hm.values()){
			//int oddCnt;
			if(value%2 != 0){
				oddCnt++;
			}
		}
		
		if (oddCnt>1){
			return false;
		}

		return true;
	}

}
