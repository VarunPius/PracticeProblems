class Solution:
    # def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        return


"""
Solution 1: simple code using PriorityQueue/heapq w/ brief explanation and analysis
- Put both slots1 and slots2 into PriorityQueue/heapq (first filter slots shorter than duration, credit to @SunnyvaleCA), sort by starting time;
- Pop out the slots one by one, comparing every consective two to check if having duration time in common.

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        s = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(s)
        while len(s) > 1:
            if heapq.heappop(s)[1] >= s[0][0] + duration:
                return [s[0][0], s[0][0] + duration] 
        return []   

Analysis

Time: O(nlog(n)), space: O(n), where n = slots1.length + slots2.length.
"""

"""
Solution 2:
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):

        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i = 0
        j = 0
        
        while i < len(slots1) and j < len(slots2):
            head = max(slots1[i][0], slots2[j][0])
            tail = min(slots1[i][1], slots2[j][1])
            if head + duration <= tail:
                return [head, head+duration]
            
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        return []
"""