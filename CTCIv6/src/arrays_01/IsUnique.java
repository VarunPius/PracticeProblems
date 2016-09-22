package arrays_01;

import java.io.*;
import java.util.Arrays;
//import java.utils.*;

public class IsUnique {
	public static void main(String args[]) throws IOException{
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter text: ");
		String orig_string = br.readLine();
		
		char[] sortArray = orig_string.toCharArray();
		Arrays.sort(sortArray);
		String sort_string = new String(sortArray);
		boolean uniqueFlag = true;
		for (int i = 0; i<sort_string.length()- 1; i++){
			if (sort_string.charAt(i) == sort_string.charAt(i+1)){
				uniqueFlag = false;
				break;
			}
		}
		if (uniqueFlag)
			System.out.println("True");
		else
			System.out.println("False");
		
	}
}
