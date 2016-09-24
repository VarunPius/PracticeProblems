package Ch01_arrays;

import java.io.*;

public class StringCompression {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter String: ");
		String str = br.readLine();

		StringBuilder cmprsd = new StringBuilder();
		int charCnt = 0;
		for (int i = 0; i<str.length(); i++){
			charCnt++;

			if ( (i+1)>=str.length() || str.charAt(i) != str.charAt(i+1) ){
				cmprsd.append(str.charAt(i));
				cmprsd.append(charCnt);
				charCnt = 0;
			}
		}

		String op = cmprsd.length() < str.length() ? cmprsd.toString():str;
		System.out.println(op);
		
	}
}
