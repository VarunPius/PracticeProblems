from collections import deque

class Solution:
    # def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    def updateMatrix(self, matrix):
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        m, n = len(matrix), len(matrix[0])

        que = deque()
        res = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    que.append([i, j])

        while que:
            curI, curJ = que.popleft()
            for i, j in dirs:
                newI, newJ = curI + i, curJ + j
                if 0 <= newI < m and 0 <= newJ < n and res[newI][newJ] == -1:
                    res[newI][newJ] = res[curI][curJ] + 1
                    que.append([newI, newJ])

        return res
