# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        return

"""
As the sorted array has an unknown size, first we need to find the search scope.
We can use a 'binary search' to find the scope: while reader.get(hi) < target: hi <<= 1 .

Here is the first decision, to choose reader.get(hi) < target or reader.get(hi) <= target.
If we choose the first one, then search scope is (hi/2, hi], otherwise [hi/2, hi). I choose the 1st one since the search scope could be half size of that of the 2nd one if target == hi.

Then we can perform the binary search and there are 4 things to decide:

    loop condition: lo < hi or lo <= hi
    lo and hi update: lo = mid + 1 or mid, hi= mid - 1 or mid
    Should loop break when target == reader.get(mid)?
    When loop ends at lo < hi or lo <= hi, what should we return?

In this problem, I want to finish my search in the loop. So if I leave loop without finding the target, I know target is not in the array and I can just return -1. This is for decision #4.

Because of decison #4 and search scope being (lo, hi], if we pick lo < hi for decision #1, when target is at hi, last loop would be lo = mid = hi-1. So reader.get(mid) < target = reader.get(hi). Then I should update lo as lo = mid + 1 otherwise it will be a dead loop. If we break out here as lo == hi, we will miss checking index hi and return -1. Thus, we need to choose lo <= hi for decision #1.
Besides, if we choose search scope as [lo, hi), we can end the loop when lo == hi.

For decision #2, we need to update as lo = mid + 1, hi= mid - 1 because of decision #1. Otherwise when target is not in array, we would stuck in loop when lo == hi.

Finally as all elements in the array are distinct so there is only one valid index to return, we could just return the index when target == reader.get(index) for decision #3.
Such return, however, would give an incorrect ansewer for some problems, such as #668. In that problem, there is a range of valid indices and we need to return a border index of that range. For example, the array is [1,3,3,3,5]and target is 3. The valid index range is [1,3] and need to return the left border index which is 1. In such case, we can't return when target == array[mid] but update as hi = mid and keep searching until lo > hi.

As you can see, there are quite a few tricky things in a binary search. You need to design carefully for each case.

def search(reader, target):
	hi = 1
	while reader.get(hi) < target: hi <<= 1
	lo = hi >> 1
	while lo <= hi:
		mid = lo + hi >> 1
		if reader.get(mid) < target: lo = mid + 1
		elif reader.get(mid) > target: hi = mid - 1
		else: return mid
	return -1

"""