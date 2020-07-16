"""
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

    numNodes, an integer representing the number of nodes in the graph.
    numEdges, an integer representing the number of edges in the graph.
    edges, the list of pair of integers - A, B representing an edge between the nodes A and B.

Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
Output: [2, 3, 5]
"""

from collections import defaultdict

class Solution:
    def getCriticalRouters(self, numNodes, edges):
        res = []

        # Construct graph
        # Initialize graph
        graph = defaultdict(list)

        # Add edges to graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        initialConnComp = 0
        visited = []
        for i in range(numNodes):
            if i not in visited:
                self.dfs(graph, i, visited)
                initialConnComp += 1
        print("Graph has ", initialConnComp, " initial components")

        # calculate critical routers
        for src in range(numNodes):
            component = 0

            # Remove each node and its edges and check if entire graph is connected
            nodeEdges = graph[src]

            for edge in nodeEdges:
                graph[edge].remove(src)

            visited = []
            for node in range(numNodes):
                if src != node and node not in visited:
                    self.dfs(graph, node, visited)
                    component += 1

            if component > initialConnComp:
                # this node was a critical router
                res.append(src)

            # add the edges back
            for edge in nodeEdges:
                graph[edge].append(src)

        return res

    def dfs(self, graph, src, visited):
        if (src in visited):
            return

        visited.append(src)
        for child in graph[src]:
            self.dfs(graph, child, visited)

if __name__ == '__main__':
    soln = Solution()
    x = soln.getCriticalRouters(7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]])
    print(x)
    x = soln.getCriticalRouters(5, [[1, 2], [0, 1], [2, 0], [0, 3], [3, 4]])
    print(x)
    x = soln.getCriticalRouters(4, [[0, 1], [1, 2], [2, 3]])
    print(x)
    x = soln.getCriticalRouters(7, [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]])
    print(x)

"""
	    int numRouters5 = 12;
	    int numLinks5 = 10;
	    int[][] links5 = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}, {7, 8}, {9, 10}, {9, 11}, {7,11}, {7, 10}};

	    List<Integer> res5 = obj.getCriticalRouters(numRouters5, numLinks5, links5);
	    for(int i: res5) System.out.print(i + " ");
	    System.out.println();
"""