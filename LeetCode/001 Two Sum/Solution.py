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
enumerate- Iterate over indices and items of a list

The Python Cookbook (Recipe 4.4) describes how to iterate over items and indices in a list using enumerate. For example:

alist = ['a1', 'a2', 'a3']

for i, a in enumerate(alist):
    print i, a

Results:

0 a1
1 a2
2 a3

zip- Iterate over two lists in parallel

I previously wrote about using zip to iterate over two lists in parallel. Example:

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b

Results:

a1 b1
a2 b2
a3 b3

enumerate with zip

Here is how to iterate over two lists and their indices using enumerate together with zip:

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print i, a, b

Results:

0 a1 b1
1 a2 b2
2 a3 b3
"""