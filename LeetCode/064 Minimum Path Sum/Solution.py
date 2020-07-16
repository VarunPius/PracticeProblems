class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])

        for i in range(1, col):         # remember the range; you did from 0, it should be from 1
            grid[0][i] += grid[0][i - 1]

        for i in range(1, row):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]


if __name__ == '__main__':
    soln = Solution()
    x = soln.minPathSum([[1,3,1], [1,5,1], [4,2,1]])
    print(x)