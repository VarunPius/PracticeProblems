class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    def canJump(self, nums):
        reach = 0

        for i, n in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + n)
        return True
