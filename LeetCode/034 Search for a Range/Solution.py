class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(lambda x, y: x >= y, nums, target) #Check parameters un function
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = self.binarySearch(lambda x, y: x>y, nums, target)
        return [left, right - 1]

    def binarySearch(self, compare, nums, target): #Compare is from lambda function
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left)//2

            if compare(nums[mid], target):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().searchRange([2, 2], 3))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
