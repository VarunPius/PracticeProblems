public class Solution {
    public int[] searchRange(int[] nums, int target) {
        if(nums == null || nums.length == 0)
            return new int[]{-1, -1};
        
        int left = 0;
        int right = nums.length;
        int mid;
        while(left < right){
            mid = left + (right - left)/2;
            
            if(nums[mid] == target){
                left = mid;
                right = mid;
                
                while (left>=0 && nums[left] ==  target)
                    left--;
                while (right<nums.length && nums[right] == target)
                    right++;
                
                return new int[]{left+1, right-1};
            }
            
            if (nums[mid]> target)
                right = mid;
            
            if (nums[mid] < target)
                left = mid+1;
        }
        
        return new int[]{-1,-1};
    }
}