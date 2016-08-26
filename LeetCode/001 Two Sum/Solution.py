class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, val in enumerate(nums):
            var1 = target - val
            if val in dict:
                return dict[val], i
            dict[var1] = i

            
"""
enumerate- Iterate over indices and items of a list:
alist = ['a1', 'a2', 'a3']

for i, a in enumerate(alist):
    print i, a

0 a1
1 a2
2 a3


zip- Iterate over two lists in parallel

I previously wrote about using zip to iterate over two lists in parallel. Example:

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b


a1 b1
a2 b2
a3 b3
"""