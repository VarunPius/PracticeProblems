import random


class Solution:
    # def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.nums = nums


    # def reset(self) -> List[int]:
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums


    # def shuffle(self) -> List[int]:
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        ans = self.nums[:]
        for i in range(len(ans)-1, 0, -1):
            j = random.randint(0, i)
            tmp = ans[i]
            ans[i] = ans[j]
            ans[j] = tmp
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
Alternative approach:
class Solution(object):
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))
"""