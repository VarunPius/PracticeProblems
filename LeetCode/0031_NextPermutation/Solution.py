class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, num):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0

        for i in range(len(num) - 1):
            if num[i] < num[i+1]:
                print("Firstloop: ", i)
                k = i

        if k == -1:
            return num.reverse()

        for i in range(k + 1, len(num)):
            if num[i] > num[k]:
                print("Secondloop: ", i)
                l = i

        print("Pre:", num)
        print("K: ", k)
        print("L: ", l)
        num[k], num[l] = num[l], num[k]
        print("Cur:", num)
        print("K2: ", k)
        num[k+1:] = num[:k:-1]
        print("Post:", num)
        return num


if __name__ == "__main__":
    num = [1, 4, 3, 2]
    print(Solution().nextPermutation(num))

'''
Debug O/p:
Firstloop:  0
Secondloop:  1
Secondloop:  2
Secondloop:  3
Pre: [1, 4, 3, 2]
K:  0
L:  3
Cur: [2, 4, 3, 1]
K2:  0
Post: [2, 1, 3, 4]
[2, 1, 3, 4]

Other Exp:
>>> a = [1,4,3,2]
>>> a[:0:-1]
[2, 3, 4]
>>> a[1:2:-1]
[]
>>> a[1:3:-1]
[]
>>> a[3:1:-1]
[2, 3]
'''

"""
def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1
"""