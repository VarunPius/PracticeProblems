class Solution:
    # def validTree(self, n: int, edges: List[List[int]]) -> bool:
    def validTree(self, n: int, edges) -> bool:
        return


"""
Solution 1:
DFS

    Simple extension of cycle finding algorithm for directed graphs. You need to include the parent as well in the DFS call.
    Now if a nbr is in visited and the nbr is not the parent, then we have a cycle.
    Notice how we build an undirected graph: include both edges.
    O(V+E)

from collections import defaultdict
class Solution(object):
    def dfs(self, node, parent, graph, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if self.dfs(nbr, node, graph, visited):
                    return True
            elif nbr in visited and nbr != parent:
                return True
        return False
    
    def validTree(self, n, edges):
        # :type n: int
        # :type edges: List[List[int]]
        # :rtype: bool
        graph = defaultdict(list)
        for edge in edges:
            u,v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        visited = set([])
        if self.dfs(0, -1, graph, visited):
            return False
        if len(visited) != n:
            return False
        return True

Union Find: Quick Find

    If an edge end points are already part of same component, then we have cycle. Also, we must make sure number of edges is equal to n-1
    Quick Find implementation of Union Find is O(V * E) - For every edge, we might have to update the entire component array which is size n

class Solution(object):
    def validTree(self, n, edges):
        # :type n: int
        # :type edges: List[List[int]]
        # :rtype: bool
        components = [i for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            pid, qid = components[u], components[v]
            if pid == qid:  # If an edge end points are in the same component, we have a cycle.
                return False
            else:
                for idx, x in enumerate(components):
                    if x == pid:
                        components[idx] = qid
        return len(edges) == n - 1 # if the number of edges are not equal to n-1, then not a tree

Union Find: Quick Union

    Quick Union is another implementation of Union Find where we build forests. For edge u,v, we find the root of u and root of v, then point root of u to root of v.
    http://algs4.cs.princeton.edu/15uf/

class Solution(object):
    def root(self, i, components):
        while i != components[i]:
            i = components[i]
        return i
    
    def validTree(self, n, edges):
        # :type n: int
        # :type edges: List[List[int]]
        # :rtype: bool
        components = [i for i in range(n)]
        for edge in edges:
            u, v = edge[0], edge[1]
            root_u, root_v = self.root(u, components), self.root(v, components)
            if root_u == root_v:  # If an edge end points are in the same component, we have a cycle.
                return False
            else:
                components[root_u] = root_v
        return len(edges) == n - 1 # if the number of edges are not equal to n-1, then not a tree

Weighted Quick Union

    Another optimization that prevents the trees from getting longer.

class Solution(object):
    def root(self, i, components):
        while i != components[i]:
            i = components[i]
        return i
    
    def validTree(self, n, edges):
        # :type n: int
        # :type edges: List[List[int]]
        # :rtype: bool
        parents = [i for i in range(n)]
        forest_size = [1]*n
        for edge in edges:
            u, v = edge[0], edge[1]
            root_u, root_v = self.root(u, parents), self.root(v, parents)
            if root_u == root_v:  # If an edge end points are in the same component, we have a cycle.
                return False
            else:
                if forest_size[root_u] < forest_size[root_v]:
                    parents[root_u] = root_v
                    forest_size[root_v] += forest_size[root_u]
                else:
                    parents[root_v] = root_u
                    forest_size[root_u] += forest_size[root_v]
        return len(edges) == n - 1 # if the number of edges are not equal to n-1, then not a tree

"""