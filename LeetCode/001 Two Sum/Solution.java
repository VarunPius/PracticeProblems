public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> mp = new HashMap <Integer, Integer>();
        int[] op = new int[2];
        for(int i = 0; i<nums.length; i++){
            int val = target - nums[i];
            
            if(mp.get(val) == null){
                mp.put(nums[i], i);
            }
            else{
                op[0] = mp.get(val);
                op[1] = i;
            }
        }
        return op;
    }
}