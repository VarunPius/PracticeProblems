public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int ans = 0;
        int sum = 0;
        
        if (nums.length <= 3){
            for (int i = 0; i<nums.length; i++){
                sum = sum + nums[i];
            }
            return sum;
        }
        
        int len = nums.length;
        
        Arrays.sort(nums);
        
        ans = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < len-2; i++){
            int j = i + 1;
            int k = len-1;
            while(j<k){
                sum = nums[i] + nums[j] + nums[k];
                if (Math.abs(target - ans) > Math.abs(target - sum)){
                    ans = sum;
                    
                    if(ans == target){      //important: forgot to do this
                        return ans;
                    }
                }
                
                if (sum>target)
                    k--;
                else
                    j++;
            }
        }
        return ans;
    }
}