from collections import defaultdict
'''
class Solution:
    #def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]      # vertex i ==> [its neighbors]
        # print(graph)                      # [[], [], [], []]
        currentRank = 0                     # please note this rank is NOT the num (name) of the vertex itself,
                                            # it is the order of your DFS level
        lowestRank = [i for i in range(n)]  # here lowestRank[i] represents the lowest order of vertex
                                            # that can reach this vertex i
        visited = [False for _ in range(n)]  # common DFS/BFS method to mark whether this node is seen before
        # print(visited)                    # [False, False, False, False]

        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        # print(graph) #[[1, 2], [0, 2, 3], [1, 0], [1]]

        return [[]]

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