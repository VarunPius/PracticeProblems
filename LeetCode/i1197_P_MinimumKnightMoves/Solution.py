class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return


"""
Clear, short and easy DP solution, No Need for BFS or math
The key observation is that we do not need to distinguish x and y, and we don't care whether x and y are positive or negative at all.

I believe it's easier than BFS or math solutions

from functools import lru_cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def DP(x,y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(DP(abs(x-1),abs(y-2)),DP(abs(x-2),abs(y-1)))+1
        return DP(abs(x),abs(y))

Thanks @kuznecpl for pointing out that we need to take care of the (1,1) and (2,0) cases properly.


Python greedy + bfs solution, 12ms beats 100%
I'd like to share my solution here in case someone is interested.

The basic idea is to make sure the total number of moves required always decrease if we move along the long edge.
I found the boundary 4 by drawing a graph, then solve the remaining number of steps by BFS.

class Solution(object):
    def minKnightMoves(self, x, y):
        '''
        :type x: int
        :type y: int
        :rtype: int
        '''
        # greedy
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            res += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2 
        # bfs        
        moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
        queue = collections.deque([(0, 0, 0)])
        while queue:
            i, j, steps = queue.popleft()
            if i == x and j == y:
                return res + steps
            for di, dj in moves:
                if (x - i) * di > 0 or (y - j) * dj > 0: # move towards (x, y) at least in one direction
                    queue.append((i + di, j + dj, steps + 1))

"""
