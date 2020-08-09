public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> rslt = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        helper(rslt, new ArrayList<Integer>(), nums, new boolean[nums.length]);
        return rslt;
    }

    public void helper(List<List<Integer>> rslt, ArrayList<Integer> mid, int[] nums, boolean[] flag){
        if(mid.size() == nums.length)
            rslt.add(new ArrayList<Integer>(mid));
        else{
            for(int i = 0;i<nums.length; i++){
                if(flag[i]||(i>0 && nums[i] == nums[i - 1] && !flag[i-1]))
                    continue;
                flag[i] = true;
                mid.add(nums[i]);
                helper(rslt, mid, nums, flag);
                flag[i] = false;
                mid.remove(mid.size() - 1);
            }
        }
    }
}
