package Ch05_Bit_Manipulation;

public class Insertion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 10245;
		int b = 13;
		System.out.println("Nos a: "+Integer.toBinaryString(a));
		System.out.println("Nos b: "+Integer.toBinaryString(b));
		int c = insertBits(a, b, 4, 12);

		System.out.println("Nos c: "+Integer.toBinaryString(c));
		
		/*
		 *  Nos a: 10100000000101
			Nos b: 1101
			Nos c: 10000011010101
		 */

	}

	public static int insertBits(int n, int m, int i, int j){
		if (i>=32|j<i)
			return 0;
			
		int allOnes = ~0;

		int left = allOnes<<(j+1);
		int right = 1<<i;
		right-=1;

		int mask = left|right;

		int n_modified = n&mask;

		int m_shifted = m<<i;

		int op = n_modified|m_shifted;

		return op;
	}

}
