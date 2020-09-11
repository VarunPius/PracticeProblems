from collections import defaultdict

class Solution:
    # def minReorder(self, n: int, connections: List[List[int]]) -> int:
    def minReorder(self, n: int, connections) -> int:
        self.visited = [0] * n
        self.graph = defaultdict(list)
        self.count = 0
        for i, j in connections:
            self.graph[i].append([j, 1])
            self.graph[j].append([i, -1])

        self.dfs(0)
        return self.count

    def dfs(self, node):
        self.visited[node] = 1
        for neib in self.graph[node]:
            if self.visited[neib[0]] == 0:
                if neib[1] == 1:
                    self.count += 1
                self.dfs(neib[0])

"""
Let us put all the edges into adjacency list twice, one with weight 1 and one with weight -1 with opposite direction.
Then what we do is just traverse our graph using usual dfs, and when we try to visit some neighbour, we check if this edge is usual or reversed.

Complexity is O(V+E), because we traverse our graph only once.

"""