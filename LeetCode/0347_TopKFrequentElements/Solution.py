from collections import Counter
from itertools import chain
import heapq

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        ct = Counter(nums).item()
        for num, freq in ct:
            bucket[freq].append(num)

        flat_list = list(chain(*bucket))

        return flat_list[::-1][:k]

    def topKFrequent2(self, nums, k):
        result = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Use Counter to extract the top k frequent elements
        # most_common(k) return a list of tuples, where the first item of the tuple is the element,
        # and the second item of the tuple is the count
        # Thus, the built-in zip function could be used to extract the first item from the tuples
        return zip(*Counter(nums).most_common(k))[0]

"""
Solution 1 is Bucket sort.
Solution 2 is using Priority Queues
Solution 3 is in-built function
"""