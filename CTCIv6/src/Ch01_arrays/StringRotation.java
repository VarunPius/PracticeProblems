package Ch01_arrays;

import java.io.*;

public class StringRotation {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		//Sort and compare is easier approach
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter String 1: ");
		String str1 = br.readLine();
		System.out.println("Enter String 2: ");
		String str2 = br.readLine();
		
		boolean op = false;
		if (str1.length() == str2.length())
			op = strRotate(str1, str2);
		//else 
			//op = false;
		
		System.out.println(op);
		
	}
	
	public static boolean strRotate(String str1, String str2){
		String tmpStr = str1 + str1;
		
		if (tmpStr.indexOf(str2) != -1)
			return true;
		
		return false;
	}

}
