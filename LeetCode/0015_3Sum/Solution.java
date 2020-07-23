public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> rslt = new ArrayList<>();
        if(nums.length<3)
            return rslt;
        
        Arrays.sort(nums);
        
        int i = 0;
        
        while (i<nums.length - 2){
            if (nums[i]>0)
                break;
            
            int sum = 0;
            int j = i+1;
            int k = nums.length - 1;
            
            while(j<k){
                sum = nums[i] + nums[j] + nums[k];
                if(sum == 0){
                    rslt.add(Arrays.asList(nums[i],nums[j], nums[k]));
                }
                if(sum <= 0){
                    while(nums[j] == nums[++j] && j<k); 	//if next sorted nos are also same 
                }
                if(sum >= 0){
                    while(nums[k--] == nums[k] && j<k); 	//if preceding sorted nos are also same
                }
            }
            
            while (nums[i]==nums[++i] && i<nums.length - 2); //if next sorted nos are also same
        }
        return rslt;
    }
}