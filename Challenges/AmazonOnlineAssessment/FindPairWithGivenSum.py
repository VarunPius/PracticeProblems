"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

    You will pick exactly 2 numbers.
    You cannot pick the same element twice.
    If you have muliple pairs, select the pair with the largest number.

Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30

Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
"""


def findPair(nums, target):
    if not nums:
        return []

    target -= 30
    dic, cand = {}, {}
    for i in range(len(nums)):
        if nums[i] in dic:
            cand[max(nums[i], target - nums[i])] = [dic[nums[i]], i]
            # cand = {40:[0,2], 50:[1,5]} for the example 2 given
        else:
            dic[target - nums[i]] = i

    return cand[max(cand.keys())]

########################################################################################

"""
Two Sum - Unique Pairs
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. 
Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2

Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
"""
def uniqueTwoSum(nums, target):
    ans, comp = set(), set()
    for n in nums:
        c = target-n
        if c in comp:
            res = (n, c) if n > c else (c, n)
            if res not in ans:
                ans.add(res)
        comp.add(n)
    return len(ans)

