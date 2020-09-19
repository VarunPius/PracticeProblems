def maxChunksToSorted(self, nums):
    sorted_nums = sorted(nums)
    count = 0
    running_difference = 0

    for i in range(len(nums)):
        running_difference += nums[i] - sorted_nums[i]
        if running_difference == 0:
            count += 1

    return count

"""

    We keep track of 2 counters X and Y - 1 for the original array, and 1 for the sorted array

original = [2, 4, 1, 6, 5, 9, 7]
sorted   = [1, 2, 4, 5, 6, 7, 9]

    As we iterate through each index, we'll increment the count of the number we see in X and Y

    As soon as X == Y, we know that we've found a new group of numbers.

from collections import defaultdict
from typing import List


def max_chunks_sorted(arr: List[int]) -> int:
    #Time  : O(N log N)
    #Space : O(1), where N = len(arr)
    
    X, Y = defaultdict(int), defaultdict(int)
    chunks = 0

    for x, y in zip(arr, sorted(arr)):
        X[x] += 1
        Y[y] += 1
        chunks += X == Y

    return chunks


if __name__ == "__main__":
    print(max_chunks_sorted([2, 4, 1, 6, 5, 9, 7]) == 3)
    print(max_chunks_sorted([4, 3, 2, 6, 1]) == 1)
    print(max_chunks_sorted([2, 1, 6, 4, 3, 7]) == 3)
"""