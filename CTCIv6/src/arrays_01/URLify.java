package arrays_01;

import java.io.*;

public class URLify {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter String: ");
		String str = br.readLine();
		System.out.println("Enter True length: ");
		int len = Integer.parseInt(br.readLine());
		
		char[] c = str.toCharArray();
		len = len-1;
		for(int i = c.length-1; i>=0; i--){
			if (c[len]!= ' '){
				c[i] = c[len];
				len--;
				continue;
			}
			else if(c[len] == ' '){
				c[i--] = '0';
				c[i--] = '2';
				c[i] = '%';
				len--;
			}
			
		}
		
		String op = new String(c);
		
		System.out.println(op);

	}

}
