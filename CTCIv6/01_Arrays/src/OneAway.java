import java.io.*;

public class OneAway {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		
		InputStreamReader isr = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(isr);
		
		System.out.println("Enter String 1: ");
		String str1 = br.readLine();
		System.out.println("Enter String 2: ");
		String str2 = br.readLine();

		boolean op = false;
		
		if(str1.length() == str2.length())
			op = checkSameLength(str1, str2);
		else if (str1.length() - 1 == str2.length())
			op = checkUnequalLength(str1, str2);
		else if (str1.length() == str2.length() - 1)
			op = checkUnequalLength(str2, str1);
		
		System.out.println(op);

	}

	public static boolean checkSameLength(String str1, String str2){
		char[] c1 = str1.toCharArray();
		char[] c2 = str2.toCharArray();

		boolean flag = true; 
		for (int i = 0; i < c1.length; i++){

			if(c1[i] != c2[i]){
				if(flag == true)
					flag = false;
				else
					return false;
			}
		}
		 return true;
	}

	public static boolean checkUnequalLength(String str1, String str2){
		char[] c1 = str1.toCharArray();
		char[] c2 = str2.toCharArray();

		boolean flag = true;

		int i = 0, j =0;

		while (i<c1.length && j<c2.length){
			if(c1[i] == c2[j]){
				i++;
				j++;
				continue;
			}

			if (c1[i] != c2[j]){
				if(flag == true){
					flag = false;
					i++;
				}
				else 
					return false;
			}
		}

		return true;
	}

}
