package Ch05_Bit_Manipulation;

import java.util.*;

public class BitSwap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter Number1: ");
		int nos1 = sc.nextInt();
		System.out.println("Number in Binary: " + Integer.toBinaryString(nos1));

		System.out.println("Enter Number2: ");
		int nos2 = sc.nextInt();
		System.out.println("Number in Binary: " + Integer.toBinaryString(nos2));

		System.out.println("O/p from first method: " + bitSwapReqd1(nos1, nos2));
		System.out.println("O/p from second method: " + bitSwapReqd2(nos1, nos2));

	}

	public static int bitSwapReqd1(int n1, int n2){
		int cnt = 0;

		for (int op = n1^n2; op!=0; op = (op>>1)){
			if((op&1)==1)
				cnt++;
		}

		return cnt;
	}

	public static int bitSwapReqd2(int n1, int n2){
		int cnt = 0;

		for (int op = n1^n2; op!=0; op=op&(op-1)){
			//if((op&1)==1)
			cnt++;
		}

		return cnt;
	}

}
