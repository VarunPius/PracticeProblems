class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        if grid is None:
            return 0
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands += 1

        return islands

    def dfs(self, grid, i, j):
        if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1'):
            return
        grid[i][j] = '#'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

def main():
    soln = Solution()
    island1 = [['1', '1', '1', '1', '0'],
               ['1', '1', '0', '1', '0'],
               ['1', '1', '0', '0', '0'],
               ['0', '0', '0', '0', '0']]
    island2 = [['1', '1', '0', '0', '0'],
               ['1', '1', '0', '0', '0'],
               ['0', '0', '1', '0', '0'],
               ['0', '0', '0', '1', '1']]
    i = soln.numIslands(island1)
    print(i)
    i = soln.numIslands(island2)
    print(i)


if __name__ == '__main__':
    main()

'''
[[1, 1, 1, 1, 0],
[1, 1, 0, 1, 0],
[1, 1, 0, 0, 0],
[0, 0, 0, 0, 0]]

[[1, 1, 0, 0, 0],
[1, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 1]]
'''