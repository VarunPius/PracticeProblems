import collections


class Solution:
    #def orangesRotting(self, grid: List[List[int]]) -> int:
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        # print(rotting)   # set([(0, 0)])
        # print(fresh)     # set([(0, 1), (2, 1), (1, 1), (2, 2), (1, 0), (0, 2)])
        timer = 0

        while fresh:
            if not rotting:
                return -1

            rotting = {(i + di, j + dj)
                       for i, j in rotting
                       for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)] if (i + di, j + dj) in fresh}
            fresh -= rotting
            timer += 1

        return timer

    def orangesRotting2(self, grid):
        n, m = len(grid), len(grid[0])
        Q = collections.deque([])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append((i,j))
        res = 0
        while Q:
            for _ in range(len(Q)):
                i, j = Q.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        cnt -= 1
                        Q.append((x,y))
            res += 1
        return max(0, res-1) if cnt == 0 else -1


if __name__ == '__main__':
    soln = Solution()
    x = soln.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    print(x)
