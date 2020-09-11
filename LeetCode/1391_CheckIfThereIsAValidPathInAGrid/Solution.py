class Solution:
    # def hasValidPath(self, grid: List[List[int]]) -> bool:
    def hasValidPath(self, grid) -> bool:
        if not grid:
            return True

        directions = {1: [(0, -1), (0, 1)],
                      2: [(-1, 0), (1, 0)],
                      3: [(0, -1), (1, 0)],
                      4: [(0, 1), (1, 0)],
                      5: [(0, -1), (-1, 0)],
                      6: [(0, 1), (-1, 0)]}
        visited = set()
        goal = (len(grid) - 1, len(grid[0]) - 1)

        def dfs(i, j):
            visited.add((i, j))
            if (i, j) == goal:
                return True
            for d in directions[grid[i][j]]:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited and (-d[0], -d[1]) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False

        return dfs(0, 0)

"""
Why (-d[0], -d[1]) in directions[grid[ni][nj]]:?

When traversing from one cell to the next. the next cell must have a direction that is the opposite of the direction we are moving in for the cells to be connected. 
For example, if we are moving one unit to the right, then from the next cell it must be possible to go one unit to the left, otherwise it's not actually connected.

"""