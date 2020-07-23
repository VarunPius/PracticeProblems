class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, rslt, min_diff, i = sorted(nums), float('Inf'), float('Inf'), 0

        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            if i == 0 or nums[i] != nums[i-1]:
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        rslt = nums[i] + nums[j] + nums[k]

                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return target
            i += 1

        return rslt

if __name__ == '__main__':
    n1 = [-1, 2, 3, 0, 1, -2, -5]
    print(Solution().threeSumClosest(n1, 10))
    print(Solution().threeSumClosest(n1, 4))
