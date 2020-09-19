"""
Give you one sorted array, please put them into n buckets, we need to ensure we get n sub array with approximately equal weights.
Example;
input {1, 2, 3, 4, 5} n = 3
output [[[5],[1,4],[2,3]];
"""

import heapq


def subset(arr, n):
    heap = [(0, i) for i in range(n)]
    res = [[] for _ in range(n)]

    for each in sorted(arr, reverse=True):
        val, idx = heapq.heappop(heap)
        total = val + each
        res[idx].append(each)

        heapq.heappush(heap, (total, idx))

    return res

ip = [1, 2, 3, 4, 5, 2, 2, 3, 9]
total_subsets = 3
print(subset(ip, total_subsets))

# 698. Partition to K Equal Sum Subsets
"""
    def canPartitionKSubsets(self, A, k):
        if len(A) < k:
            return False
        ASum = sum(A)
        A.sort(reverse=True)
        if ASum % k != 0:
            return False
        target = [ASum / k] * k

        def dfs(pos):
            if pos == len(A): return True
            for i in xrange(k):
                if target[i] >= A[pos]:
                    target[i] -= A[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += A[pos]
            return False
        return dfs(0)

Solution 2:
Utilizes "empty bucket" trick by @chengyuge925 from here.
Recursively checks whether element i fits either of subsets.

Surprisingly, removing of "empty bucket" trick makes it slowest python solution.

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        sums = [0]*k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in xrange(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False        
        
        return walk(0)

"""