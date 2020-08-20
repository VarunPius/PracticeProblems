# Using Iterative DFS
from collections import deque
import heapq


def dfs(curr_ver, graph, visited):
    stack = deque()
    stack.append(curr_ver)
    res = []
    visited.add(curr_ver)
    while stack:

        node = stack.pop()
        heapq.heappush(res, node)

        for ver in graph[node]:
            if ver not in visited:
                visited.add(ver)
                stack.append(ver)

    return res, visited


def largest_item_associations(arr):
    if not arr: return []

    graph = {}
    edges = set()
    for i, edge in enumerate(arr):
        edge1 = edge[0]
        edge2 = edge[1]

        if edge1 not in graph:
            graph[edge1] = []
            edges.add(edge1)
        if edge2 not in graph:
            graph[edge2] = []
            edges.add(edge2)

        graph[edge1].append(edge2)
        graph[edge2].append(edge1)

    visited = set()
    out = []

    for node in graph:
        if node not in visited:
            res, visited = dfs(node, graph, visited)

        if not out:
            out.append(res[:])
        elif len(out[0]) < len(res):
            out.pop()
            out.append(res[:])
        elif len(out[0]) == len(res) and " ".join(out[0]) > " ".join(res):
            out.pop()
            out.append(res[:])
    return out