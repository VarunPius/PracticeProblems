class Solution:
    # def findCircleNum(self, M: List[List[int]]) -> int:
    def findCircleNum(self, M) -> int:
        ans = 0
        visited = set()
        row = len(M)
        def dfs(i):
            for nei, adj in enumerate(M[i]):
                if adj and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                ans += 1

        return ans

    def findCircleNum2(self, M):
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    cur = toSee.pop()
                    if cur not in seen:
                        seen.add(cur)
                        toSee = [j for j, v in enumerate(M[cur]) if v and j not in seen] + toSee
                res += 1
        return res


"""
From some source, we can visit every connected node to it with a simple DFS.
As is the case with DFS's, seen will keep track of nodes that have been visited.

For every node, we can visit every node connected to it with this DFS, and increment our answer as that represents one friend circle (connected component.)
"""
