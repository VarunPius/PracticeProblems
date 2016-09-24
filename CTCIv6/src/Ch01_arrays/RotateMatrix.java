package Ch01_arrays;

public class RotateMatrix {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[][] mtrx = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

		//boolean op = false;

		if (mtrx.length == mtrx[0].length)
			rotate(mtrx);
		for(int i = 0; i < mtrx.length; i++){
			for(int j = 0; j< mtrx[0].length; j++){
				System.out.print(mtrx[i][j]);
			}
		}
		//System.out.println(mtrx);
	}

	public static void rotate(int[][] mtrx){
		int len = mtrx.length;

		for (int n = 0; n < len/2; n++){
			int first = n;
			int last = len - 1 - n;

			for (int i = first; i<last; i++){
				
				int offset = last - i;
				int tmp = mtrx[first][i];

				mtrx[first][i] = mtrx[offset-first][first];
				mtrx[offset-first][first] = mtrx[last][offset-first];
				mtrx[last][offset-first] = mtrx[i][last];
				mtrx[i][last] = tmp;
				

				/*
				int offset = i - first;
				int tmp = mtrx[first][i];

				mtrx[first][i] = mtrx[offset][first];
				mtrx[offset][first] = mtrx[last][offset];
				mtrx[last][offset] = mtrx[last][i];
				*/
			}
		}
	}
}
