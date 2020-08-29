from collections import defaultdict

class Solution:
    # def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
    def numBusesToDestination(self, routes, S: int, T: int) -> int:
        to_routes = defaultdict(set)

        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)

        bfs = [(S, 0)]
        seen = set([S])

        for stop, bus in bfs:
            if stop == T: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []
        return -1


"""
Alternate Solution1:
# Reference: https://leetcode.com/problems/bus-routes/discuss/122712/Simple-Java-Solution-using-BFS
from collections import deque
class Solution:
    # This is a very good BFS problem.
    # In BFS, we need to traverse all positions in each level firstly, and then go to the next level.
    # Our task is to figure out:
    # 1. What is the level in this problem?
    # 2. What is the position we want in this problem?
    # 3. How to traverse all positions in a level?
    # 
    # For this problem:
    # 1. The level is each time to take bus.
    # 2. The position is all of the stops you can reach for taking one time of bus.
    # 3. Using a queue to record all of the stops can be arrived for each time you take buses.
    def numBusesToDestination(self, routes, S, T):
        # :type routes: List[List[int]]
        # :type S: int
        # :type T: int
        # :rtype: int
        
        # You already at the terminal, so you needn't take any bus.
        if S == T: return 0
        
        # You need to record all the buses you can take at each stop so that you can find out all
        # of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        stopBoard = {} 
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)
        
        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([S])
        # Using visited to record the buses that have been taken before, because you needn't to take them again.
        visited = set()

        res = 0
        while queue:
            # take one time of bus.
            res += 1
            # In order to traverse all of the stops you can reach for this time, you have to traverse
            # all of the stops you can reach in last time.
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in stopBoard[curStop]:
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T: return res
                        queue.append(stop)
        return -1
"""

