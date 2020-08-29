class Solution:
    # def getMaximumGold(self, grid: List[List[int]]) -> int:
    def getMaximumGold(self, grid) -> int:
        def dfs(x, y, sum):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 0 or grid[x][y] > 100:
                return sum
            sum += grid[x][y]
            grid[x][y] += 100
            mx = 0
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                mx = max(dfs(i, j, sum), mx)
            grid[x][y] -= 100
            return mx


        row, col = len(grid), len(grid[0])
        return max(dfs(i, j, 0) for j in range(col) for i in range(row))
