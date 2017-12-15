# Time:  O(n^2)
# Space: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        cnt, k = 0, 2

        while k < n:
            i, j = 0, k - 1

            while i < j:
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    cnt += j - i
                    i += 1
            k +=1
        return cnt

if __name__ == '__main__':
    n1 = [-1, 2, 3, 0, 1, -2, -5]
    n2 = [-2, 0, 1, 3]
    print(Solution().threeSumSmaller(n1, 4))
    print(Solution().threeSumSmaller(n2, 2))
