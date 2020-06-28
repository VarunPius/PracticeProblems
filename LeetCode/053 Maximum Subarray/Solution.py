class Solution:
    #def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        # if lowest sum needed irrespective of whether it is negative or not
        currSum = maxSum = nums[0]

        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum

    def maxSubArray2(self, nums):
        # if negative sum not allowed
        currSum = maxSum = 0
        for num in nums:
            currSum = currSum + num
            if maxSum < currSum:
                maxSum = currSum
            elif currSum < 0:
                currSum = 0
        return maxSum


if __name__ == '__main__':
    soln = Solution()
    i = soln.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])
    #i = soln.maxSubArray2([-2,-3,-1,-5])
    print(i)