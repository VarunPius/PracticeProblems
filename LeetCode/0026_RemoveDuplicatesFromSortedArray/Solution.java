public class Solution {
    public int removeDuplicates(int[] nums) {
        int curr = 1;
        
        if (nums.length == 0 || nums == null)
            return 0;
        
        if (nums.length == 1)
            return 1;
        
        
        for (int i = 1; i<nums.length; i++){
            if (nums[i] != nums[i-1])
                nums[curr++] = nums[i];
        }
        
        return curr;
    }
}