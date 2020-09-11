class Solution:
    # def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    def makeConnected(self, n: int, connections) -> int:
        if n-1 > len(connections): return -1
        G = [set() for _ in range(n)]
        for i, j in connections:
            G[i].add(j)
            G[j].add(i)
        seen = [0]*n

        def dfs(i):
            print(i)
            if seen[i]: return 0
            seen[i] = 1
            for j in G[i]:
                dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1


if __name__ == '__main__':
    soln = Solution()
    x = soln.makeConnected(4, [[0,1],[0,2],[1,2]])
    print(x)


"""
[[0,1],[0,2],[1,2]]

Explanation
We need at least n - 1 cables to connect all nodes (like a tree).
If connections.size() < n - 1, we can directly return -1.

One trick is that, if we have enough cables,
we don't need to worry about where we can get the cable from.

We only need to count the number of connected networks.
To connect two unconneccted networks, we need to set one cable.

The number of operations we need = the number of connected networks - 1


Complexity
Time O(connections)
Space O(n)
"""