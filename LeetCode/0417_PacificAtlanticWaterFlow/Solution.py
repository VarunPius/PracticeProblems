class Solution:
    # def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n - 1, a_visited, m, n)

        for j in range(n):
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m - 1, j, a_visited, m, n)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i, j])

        return ans

    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in dir:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)