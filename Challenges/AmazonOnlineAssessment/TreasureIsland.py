"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""

from collections import deque
def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    matrix = [row[:] for row in m]
    nrow, ncol = len(matrix), len(matrix[0])

    q = deque([((0, 0), 0)])  # ((x, y), step)
    matrix[0][0] = "D"
    while q:
        (x, y), step = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                if matrix[x+dx][y+dy] == "X":
                    return step+1
                elif matrix[x+dx][y+dy] == "O":
                    # mark visited
                    matrix[x + dx][y + dy] = "D"
                    q.append(((x+dx, y+dy), step+1))

    return -1

############################################################################################

"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
"""

from collections import deque


class solution:
    def shortestPath(self, grid):
        if not grid or not grid[0]:
            return 0

        res = float('inf')
        row, col = len(grid), len(grid[0])
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'S':
                    q = deque([[i, j, 0]])
                    res = min(self.bfs(q, grid, row, col), res)
        return res

    def bfs(self, q, grid, row, col):
        visited = [[-1 for _ in range(col)] for _ in range(row)]
        while len(q):
            i, j, step = q.popleft()
            visited[i][j] = step
            if grid[i][j] == 'X':
                return step

            for d in self.directions:
                next_i, next_j = i + d[0], j + d[1]
                if next_i >= 0 and next_i < row and next_j >= 0 and next_j < col:
                    if grid[next_i][next_j] != 'D' and visited[next_i][next_j] == -1:
                        q.append([next_i, next_j, step + 1])
        return -1
