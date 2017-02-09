public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> rslt = new ArrayList<List<Integer>>();
        Arrays.sort(candidates);
        helper(rslt, new ArrayList<Integer>(), candidates, target, 0);
        return rslt;
    }
    
    public void helper(List<List<Integer>> rslt, ArrayList<Integer> mid, int[] nums, int currVal, int start){
        if(currVal < 0)
          return;
        else if(currVal == 0){
          rslt.add(new ArrayList<>(mid));
          //return;
        }
        else{
          for(int i = start; i<nums.length; i++){
            mid.add(nums[i]);           //to be discussed
            helper(rslt, mid, nums, currVal - nums[i], i);
            mid.remove(mid.size() - 1);
          }
          //return;
        }
          
    }
}