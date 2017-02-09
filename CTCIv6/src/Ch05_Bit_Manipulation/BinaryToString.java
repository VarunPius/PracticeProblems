package Ch05_Bit_Manipulation;

import java.util.*;

public class BinaryToString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a number: ");
		double num = sc.nextDouble();
		String op = printBinary(num);
		System.out.println("Binary Representation: " + op);
		
		/*Enter a number: 
			0.32
			Binary Representation: .010100011110101110000101000111101011100001010001111011
		*/
	}

	public static String printBinary(double num){
		if(num<=0 || num>=1)
			return "ERROR";

		StringBuilder bin = new StringBuilder();
		bin.append(".");
		double t = 0; // = num*2;
		while(num>0){
			if(bin.length()>48)
				return "ERROR";

			t = num*2;

			if(t >= 1){
				bin.append(1);
				num = t - 1;
			}
			else{
				bin.append(0);
				num = t;
			}
		}
		return bin.toString();
	}
}
