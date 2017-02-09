package Ch05_Bit_Manipulation;

import java.util.*;

public class PairwiseSwap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Number: ");
		int nos = sc.nextInt();
		System.out.println("Nos: "+Integer.toBinaryString(nos));
		int op = swapNos(nos);
		System.out.println("Swapped Nos: "+op+" Binary Nos: "+Integer.toBinaryString(op));

	}

	public static int swapNos(int nos){
		return ((nos&0xAAAAAAAA)>>>1)|((nos&0x55555555)<<1);
	}

}
