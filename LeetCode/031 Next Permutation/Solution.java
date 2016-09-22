public class Solution {
    public void nextPermutation(int[] nums) {
        if (nums.length <= 1)
            return;

        int i = nums.length - 1;

        for(; i>0; i--){
        	if(nums[i]>nums[i-1])
        		break;
        }

        if(i != 0){
        	int x = nums.length - 1;

        	for(; x>=i; x--){
        		if (nums[x] > nums[i-1])
        			break;
        	}
        	swap(nums, i-1, x);
        }
        reverseSet(nums, i, nums.length - 1);
    }

    public void swap(int[] num, int i, int j){
    	int t = num[i];
    	num[i] = num[j];
    	num[j] = t;
    }

    public void reverseSet(int[] num, int i, int j){
    	for (; i<j; i++, j--){
    		swap(num, i, j);
    	}
    }

}