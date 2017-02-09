public class Solution {
    public String addBinary(String a, String b) {
        char[] aArr = a.toCharArray();
        char[] bArr = b.toCharArray();

        char[] sumArr = new char[Math.max(aArr.length, bArr.length) + 1];

        int idx = sumArr.length - 1;
        int carry = 0;
        int sum = 0;

        for(int aIdx = aArr.length - 1, bIdx = bArr.length - 1; aIdx>=0||bIdx >= 0; aIdx--, bIdx--){
        	int aNum = aIdx<0 ? 0:aArr[aIdx] - '0';  //Mistake here
        	int bNum = bIdx<0 ? 0:bArr[bIdx] - '0';  //Mistake here

        	sum = aNum + bNum + carry;
        	sumArr[idx--] = (char)('0' + sum%2);    //Mistake here. not '0' + (char)sum%2 but as mentioned.
        	carry = sum/2;
        }

        sumArr[0] = (char)('0' + carry);        //Mistake here.
        return carry == 0 ? new String(sumArr,1, sumArr.length -1) : new String(sumArr);
    }
}
