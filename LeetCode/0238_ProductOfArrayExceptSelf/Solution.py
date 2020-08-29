class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []

        for i in range(n):
            output.append(p)
            p = p * nums[i]

        p = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output

"""
Very basic idea and raw code without more trick, the core behind it is the first loop get the product before the element 
and the second loop get the product after the element.

"""