class Solution:
    # def jump(self, nums: List[int]) -> int:
    def jump(self, nums) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times

"""
The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
right = max(i + nums[i] for i in range(left, right + 1)
"""