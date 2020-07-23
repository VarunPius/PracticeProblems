public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> rslt = new ArrayList<List<Integer>>();
        //Arrays.sort(nums);
        helper(rslt, new ArrayList<Integer>(), nums);
        return rslt;
    }

    public void helper(List<List<Integer>> rslt, ArrayList<Integer> mid, int[] nums){
        if(mid.size() == nums.length)
            rslt.add(new ArrayList<Integer>(mid));
        else{
            for(int i = 0;i<nums.length; i++){
                if(mid.contains(nums[i]))
                    continue;
                mid.add(nums[i]);
                helper(rslt, mid, nums);
                mid.remove(mid.size() - 1);
            }
        }
    }
}
