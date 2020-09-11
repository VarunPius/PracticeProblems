from collections import defaultdict


class Solution:
    # DFS
    # def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        subordinates = defaultdict(list)
        for i, emp in enumerate(manager):
            if emp != -1:
                subordinates[emp].append(i)

        self.ans = 0
        def dfs(man, time):
            self.ans = max(self.ans, time)
            for sub in subordinates[man]:
                dfs(sub, time + informTime[man])

        dfs(headID, 0)
        return self.ans


if __name__ == '__main__':
    soln = Solution()
    x = soln.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0])
    print(x)

"""
Alternate Solutions:

Top Down DFS:
dfs find out the time needed for each employees.
The time for a manager = max(manager's employees) + informTime[manager]
Time O(N), Space O(N)

    def numOfMinutes(self, n, headID, manager, informTime):
        children = [[] for i in xrange(n)]
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)

Bottom Up DFS:
    def numOfMinutes(self, n, headID, manager, informTime):
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i])
                manager[i] = -1
            return informTime[i]
        return max(map(dfs, range(n)))
"""

"""
Solution2:

Dijkstra
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for i, managerId in enumerate(manager):
            graph[managerId].append((informTime[i], i))
        
        dist = {}
        heap = [(informTime[headID], headID)] 
        
        while heap:
            time, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = time    
            for w, v in graph[u]:
                if v in dist:
                    continue
                heapq.heappush(heap, (time+w, v))    
        return max(dist.values()) 

BFS
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res
"""

"""
Solution3:
BFS
Clone informTime and build subordinates relations;
Starting from headID, the root, do BFS to find the max time needed to reach the leaves.
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates, time = collections.defaultdict(list), informTime[:]
        for i, m in enumerate(manager):
            if m >= 0:
                subordinates.setdefault(m,[]).append(i)
        dq, ans = collections.deque([headID]), 0
        while dq:
            e = dq.popleft()
            if manager[e] >= 0:
                time[e] += time[manager[e]]        
            ans = max(ans, time[e])
            if subordinates[e]:
                dq.extend(subordinates[e])
        return ans

DFS
Build subordinates relations;
Starting from headID, the root, do DFS to find the max time needed to reach the leaves.
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(id: int) -> int:
            return max(informTime[id] + dfs(sub) for sub in subordinates[id]) if id in subordinates else 0
        
        subordinates = collections.defaultdict(list)
        for i, m in enumerate(manager):
            if i != headID:
                subordinates.setdefault(m,[]).append(i)
        return dfs(headID)

Analysis:
Time & space: O(n), where n = manager.length.
"""