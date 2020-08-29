class Solution:
    # def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    def findSmallestSetOfVertices(self, n: int, edges):
        return list(set(range(n)) - set(j for _, j in edges))

"""
Intuition
Just return the nodes with no in-degres.

Explanation
Quick prove:

All nodes with no in-degree must in the final result,
because they can not be reached from
All other nodes can be reached from any other nodes.
All other nodes can be reached from some other nodes.

Complexity
Time O(E)
Space O(N)
"""