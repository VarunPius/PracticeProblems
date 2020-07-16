"""
Min Cost to Connect All Nodes
Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes already connected by an edge.
newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).
Example 1:

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7
Explanation:
There are 3 connected components [1, 4, 5], [2, 3] and [6].
We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.

"""
import collections
import heapq

# Prim's algo:
def minCostToConnectAllNodes(self, n, edges, newEdges):
    q = [(0, n)]
    visited = set()
    G = collections.defaultdict(list)
    for edge in edges:
        G[edge[0]].append((0, edge[1]))
        G[edge[1]].append((0, edge[0]))
    for edge in newEdges:
        G[edge[0]].append((edge[2], edge[1]))
        G[edge[1]].append((edge[2], edge[0]))
    total = 0
    while q and len(visited) < n:
        cost1, v1 = heapq.heappop(q)
        if v1 not in visited:
            visited.add(v1)
            total += cost1
            for cost2, v2 in G[v1]:
                heapq.heappush(q, (cost2, v2))
    return total

"""
Kruskal's algo:
def merge_groups(groups: List[Set[int]], group_ids: List[int]) -> None:
    '''
    Merge 2 groups with ids group_ids[0] and group_ids[1]
    '''

    # Sort so we don't screw up indexing for the 2nd pop() call
    group_ids.sort()
    groups.append(groups.pop(group_ids[1]).union(
        groups.pop(group_ids[0])))


def connection_cost(n: int, edges: List[List[int]], new_edges: List[List[int]]) -> int:
    ''' 
    Use Kruskal's algorithm to add all exiting and new edges to a new graph
    '''

    # assign zero weight to existing edges
    edges = [[f, t, 0] for f, t in edges]
    # Merge existing and new edges
    edges += new_edges
    # Sort by edge weights
    edges.sort(key=lambda edge: edge[2])

    total_cost = 0
    # Initially, each node is in its own group
    groups = [{i} for i in range(1, n+1)]
    while edges:
        # new_edge is the one with lowest weight since edges list is sorted
        new_edge = edges.pop(0)

        # Look for groups that contain nodes from the edge we're exploring
        group_ids = []
        for (group_index, group) in enumerate(groups):
            if new_edge[0] in group or new_edge[1] in group:
                group_ids.append(group_index)
                # Both nodes are from the same group, or 2 groups already found. No need to keep looking
                if new_edge[0] in group and new_edge[1] in group or len(group_ids) >= 2:
                    break
        # The edge connects 2 existing groups. We need to merge them
        if len(group_ids) > 1:
            merge_groups(groups, group_ids)
            total_cost += new_edge[2]
    return total_cost
"""

#########################################################################################
"""
Min Cost to Repair Edges
There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting the graph. Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes connected by an edge.
edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12).
Example 1:

Input: n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
Output: 20
Explanation:
There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.
Example 2:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], edgesToRepair = [[1, 6, 410], [2, 4, 800]]
Output: 410
Example 3:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
Output: 79
"""

from collections import defaultdict
import heapq

class Solution:
    def __init__(self):
        pass

    def minCostForRepair(self, n, edges, edgesToRepair):
        graph = defaultdict(list)
        addedEdges = set()
        for edge in edgesToRepair:
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
            addedEdges.add((edge[0], edge[1]))
            addedEdges.add((edge[1], edge[0]))
        for edge in edges:
            if tuple(edge) not in addedEdges:
                graph[edge[0]].append((0, edge[1]))
                graph[edge[1]].append((0, edge[0]))

        res = 0
        priorityQueue = [(0, 1)]
        heapq.heapify(priorityQueue)
        visited = set()

        while priorityQueue:
            minCost, node = heapq.heappop(priorityQueue)
            if node not in visited:
                visited.add(node)
                res += minCost
                for cost, connectedNode in graph[node]:
                    if connectedNode not in visited:
                        heapq.heappush(priorityQueue, (cost, connectedNode))

        return res


s = Solution()

print(s.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))