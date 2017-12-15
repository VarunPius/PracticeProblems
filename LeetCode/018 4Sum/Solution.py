class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        rslt = []

        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1
                sum = target - nums[i] - nums[j]

                while left < right:
                    if nums[left] + nums[right] == sum:
                        rslt.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] < sum:
                        left += 1
                    else:
                        right -= 1
        return rslt

if __name__ == '__main__':
    result = Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
    print(result)
    n1 = [0, 0, 0, 0]
    print(Solution().fourSum(n1, 0))
