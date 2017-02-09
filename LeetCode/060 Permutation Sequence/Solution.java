public class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> nos = new ArrayList<Integer>();
        int[] fact = new int[n+1];
        int sum = 1;
        StringBuilder sb = new StringBuilder();

        fact[0] = 1;
        for(int i = 1; i<=n; i++){
            sum*=i;
            fact[i] = sum;
            nos.add(i);
        }

        k--;

        for(int i = 1; i<=n; i++){
            int idx = k/fact[n-i];
            sb.append(String.valueOf(nos.get(idx)));
            nos.remove(idx);
            k-=(idx*fact[n-i]);
        }

        return sb.toString();
    }
}