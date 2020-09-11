class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j]:
                grid[i][j] == 0
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0

        areas = [dfs(x, y) for x in range(row) for y in range(col) if grid[x][y]]

        return max(areas) if areas else 0

