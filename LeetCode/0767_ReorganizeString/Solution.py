import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        max_freq = Counter(S).most_common(1)[0][1] # most_common format is [(word, freq)]
        if 2*max_freq - 1 > len(S):
            return ""
        else:
            heap = []
            result = []
            for k, v in Counter(S).items():
                heapq.heappush(heap, (-1*v, k))
            while heap:
                v, k = heapq.heappop(heap)
                if not result or k != result[-1]:   # can add the top-most element from heap
                    result.append(k)
                    if v != -1:
                        heapq.heappush(heap, (v + 1, k))
                else:                               # cannot add the top most element
                    v1, k1 = heapq.heappop(heap)
                    result.append(k1)
                    heapq.heappush(heap, (v, k))
                    if v1 != -1:
                        heapq.heappush(heap, (v1 + 1, k1))

            return "".join(result)


"""
Algorithm

Say most frequently occuring character (say c) has frequency max_freq.
Then arrange c leaving a space between consecutive c's.
The remaining characters should be more than the number of spaces for a valid arrangement.
This means that max_freq + (max_freq-1) <= len(S).
We can test this quickly using Counter class from collections module and using the mostcommon(i) method which returns a list i most frequent tuples.

Now we create an array called result to store the result.
We add (freq*-1,char) tuples to a heap (this is how we simulate a max-heap in Python using a min-heap.
We then pick the most frequent element and if that element is not the last element in the result, we add it to result, If it is the last element of the result, then we pick the second most frequent element and add that to the result, and also add back the most frequent element back to the heap.
Note when we pop from the heap and utilize the character in the result, we need to add it back to the heap if the frequency is not -1 (-1 means that only one instance of that element was in the heap and we have now used it, so no need to add it back).

Time Complexity is O(N * lg(A)).
    N is the length of the string.
    A is the size of the alphabet.
    The size of the heap will be at-most A.
But since we remove and add back elements such that at each iteration we only add one character to the result, there will be N * lg(A) calls.
Since A is fixed, we can assume complexity to be O(N).

Space is also O(A).
"""
