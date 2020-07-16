from collections import defaultdict


class Solution:
    # def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    def criticalConnections(self, n, connections):
        res = []
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        lowestRank = [i for i in range(n)]
        currentRank = 0
        prevNode = -1
        currNode = 0

        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])


        self.dfs(res, graph, visited, lowestRank, currentRank, prevNode, currNode)

        return res

    def dfs(self, res, graph, visited, lowestRank, currentRank, prevNode, currNode):
        visited[currNode] = True
        lowestRank[currNode] = currentRank

        for nextNode in graph[currNode]:
            if nextNode == prevNode:
                continue

            if not visited[nextNode]:
                self.dfs(res, graph, visited, lowestRank, currentRank + 1, currNode, nextNode)

            lowestRank[currNode] = min(lowestRank[currNode], lowestRank[nextNode])

            if lowestRank[nextNode] >= currentRank + 1:
                res.append([currNode, nextNode])


if __name__ == '__main__':
    soln = Solution()
    i = soln.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])


'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

		graph = [[] for _ in range(n)] ## vertex i ==> [its neighbors]
		
        currentRank = 0 ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
		
        lowestRank = [i for i in range(n)] ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
		
        visited = [False for _ in range(n)] ## common DFS/BFS method to mark whether this node is seen before
        
        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        res = []
        prevVertex = -1 ## This -1 a dummy. Does not really matter in the beginning. 
		## It will be used in the following DFS because we need to know where the current DFS level comes from. 
		## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.
		
        currentVertex = 0 ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res
    
    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):

        visited[currentVertex] = True 
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
				# We avoid visiting visited nodes here instead of doing it at the beginning of DFS - 
				# the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex]) 
			# take the min of the current vertex's and next vertex's ranking
            if lowestRank[nextVertex] >= currentRank + 1: ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])

    def criticalConnections2(self, n, connections):
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        # print(graph) # defaultdict(<type 'list'>, {0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1]})

        dfn = [None for i in range(n)]
        low = [None for i in range(n)]

        res = []
        self.cur = 0

        def dfs(node, parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    if dfn[n] is None:
                        dfs(n, node)

                if parent is not None:
                    l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    l = min(low[i] for i in graph[node] + [low[node]])
                low[node] = l

        dfs(0, None)

        for v in connections:
            if low[v[0]] > dfn[v[1]] or low[v[1]] > dfn[v[0]]:
                res.append(v)
        return res


if __name__ == '__main__':
    soln = Solution()
    x = soln.criticalConnections2(4, [[0,1],[1,2],[2,0],[1,3]])
    print(x)
'''