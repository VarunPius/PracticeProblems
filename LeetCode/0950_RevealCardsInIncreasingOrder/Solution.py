from collections import deque
class Solution:
    # def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    def deckRevealedIncreasing(self, deck):
        d = deque()
        for x in sorted(deck)[::-1]:
            d.rotate()
            d.appendleft(x)
        return list(d)


"""
We simulate the reversed process.
Initial an empty list or deque or queue,
each time rotate the last element to the first,
and append a the next biggest number to the left.

Time complexity:
O(NlogN) to sort,
O(N) to construct using deque or queue.
"""

"""
Solution 2:
Python, using list, O(N^2):
    def deckRevealedIncreasing(self, deck):
        d = []
        for x in sorted(deck)[::-1]:
            d = [x] + d[-1:] + d[:-1]
        return d
"""
