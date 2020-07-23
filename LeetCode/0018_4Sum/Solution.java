public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int len = nums.length;
        ArrayList<List<Integer>> rslt = new ArrayList<List<Integer>>();

        if(nums == null || len<4)
            return rslt;

        Arrays.sort(nums);

        int max = nums[len-1];

        if (4*nums[0]>target || 4*max<target)   //numbers wont add up to target as greater or less than target
            return rslt;

        for (int i = 0; i< len; i++){
            int z = nums[i];

            if (i>0 && z == nums[i-1])
                continue;
            if (z + (3*max) < target)
                continue;
            if (4*z > target)
                break;
            if (4*z == target){
                if( i+3 < len && nums[i+3] == z)
                    rslt.add(Arrays.asList(z,z,z,z));

                break;
            }

            threeSum(nums, i+1, len-1, target - z, z, rslt);

        }
        return rslt;
    }

    public void threeSum(int[] nums, int low, int high, int newTarget, int z1, ArrayList<List<Integer>> rslt){
        if (low+1 >=high)
            return;

        int max = nums[high];

        if(3*nums[low] > newTarget || 3*max < newTarget)
            return;

        for (int i = low; i <= high; i++){
            int z = nums[i];

            if(i > low && z == nums[i-1])
                continue;
            if(z + (2*max) < newTarget)
                continue;
            if (3*z > newTarget)
                break;
            if (3*z == newTarget) {
                if( i + 1 < high && nums[i+2] == z)
                    rslt.add(Arrays.asList(z1,z,z,z));

                break;
            }

            twoSum(nums, i+1, high, newTarget - z, z1, z, rslt);

        }
    }

    public void twoSum(int[] nums, int low, int high, int newTarget, int z1, int z2, ArrayList<List<Integer>> rslt){
        if (low >= high)
            return;

        if (2*nums[low] > newTarget || 2*nums[high] < newTarget)
            return;

        int i = low;
        int j = high;

        int sum, x;

        while(i<j){
            sum = nums[i] + nums[j];

            if(sum == newTarget){
                rslt.add(Arrays.asList(z1, z2, nums[i], nums[j]));

                x = nums[i];
                while (++i < j && x == nums[i])
                    ;

                x = nums[j];
                while (i < --j && x == nums[j]);
            }
            if (sum< newTarget)
                i++;
            if (sum > newTarget)
                j--;
        }
        return;
    }
}


/*
Input:
[-1,0,1,2,-1,-4]
-1
Output:
[[-4,0,1,2]]
Expected:
[[-4,0,1,2],[-1,-1,0,1]]
*/
