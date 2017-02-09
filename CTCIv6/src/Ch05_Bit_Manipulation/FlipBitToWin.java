package Ch05_Bit_Manipulation;

import java.util.*;

public class FlipBitToWin {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter nos");
		int nos = sc.nextInt();
		int op = longestSequence(nos);

		System.out.println(op);

	}

	public static int longestSequence(int nos){
		if (nos == -1) return Integer.BYTES*8;  //Chk if all 1s
		ArrayList<Integer> seq = getSequence(nos);
		return evalLongestSeq(seq);
	}

	public static ArrayList<Integer> getSequence(int nos){
		List<Integer> seq = new ArrayList<Integer>();

		int elem = 0;
		int cnt = 0;

		for (int i = 0; i<Integer.BYTES*8; i++){
			if((nos&1) != elem){
				seq.add(cnt);
				elem = nos&1;
				cnt = 0;
			}
			cnt++;
			nos>>>=1;
		}
		seq.add(cnt);
		return (ArrayList<Integer>)seq;
	}

	public static int evalLongestSeq(ArrayList<Integer> seq){
		int maxSeq = 1;

		for(int i = 0; i<seq.size(); i+=2){
			int zeroSeq = seq.get(i);
			int oneSeqRight = i>0?seq.get(i-1):0;
			int oneSeqLeft = i+1==seq.size()?seq.get(0):seq.get(i+1);
			int thisSeq = 0;
			if(zeroSeq == 1){
				thisSeq = oneSeqLeft + 1 + oneSeqRight;
			}
			else if (zeroSeq>1){
				thisSeq = 1+ Math.max(oneSeqLeft, oneSeqRight);
			}
			else if(zeroSeq == 0){
				thisSeq = Math.max(oneSeqLeft, oneSeqRight);
			}
			maxSeq = Math.max(maxSeq, thisSeq);
		}

		return maxSeq;

	}

}
