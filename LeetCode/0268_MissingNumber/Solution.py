class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

"""
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)

"""