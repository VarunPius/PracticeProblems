# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


"""
For a sorted array, the left half will be in the left subtree, middle value as the root, right half in the right subtree.
This holds true for every node:

[1, 2, 3, 4, 5, 6, 7] -> left: [1, 2, 3], root: 4, right: [5, 6, 7]
[1, 2, 3] -> left: [1], root: 2, right: [3]
[5, 6, 7] -> left: [5], root: 6, right: [7]

Many of the approaches here suggest slicing an array recursively and passing them. However, slicing the array is expensive. 
It is better to pass the left and right bounds into recursive calls instead.

class Solution(object):
    def sortedArrayToBST(self, nums):
        # Time: O(n)
        # Space: O(n) in the case of skewed binary tree.
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        return convert(0, len(nums) - 1)
"""