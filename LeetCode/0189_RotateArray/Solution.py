class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    #def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k%len(nums)

        i = len(nums) - k
        self.reverse(nums, 0, i - 1)
        self.reverse(nums, i, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        return nums

    
    def reverse(self, nums, left, right):
        while (left < right):
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left = left + 1
            right = right - 1


def main():
    soln = Solution()

if __name__ == "__main__":
    main()

# 1 2 3 4 5 6 > 5 6 1 2 3 4