class Solution:
    def numDistinctIslands(self, grid):
        if not grid:
            return 0

        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                st = set()
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, i, j, st)
                    print(st)
                    res.append(st)
                    # res.add(str(st))
        print(res)
        return len(res)

    def dfs(self, grid, i, j, baseX, baseY, set):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return

        set.add(str(i - baseX) + "_" + str(j - baseY))
        grid[i][j] = 0
        self.dfs(grid, i + 1, j, baseX, baseY, set)
        self.dfs(grid, i - 1, j, baseX, baseY, set)
        self.dfs(grid, i, j + 1, baseX, baseY, set)
        self.dfs(grid, i, j - 1, baseX, baseY, set)



if __name__ == '__main__':
    soln = Solution()
    island1 = [[1, 1, 1, 1, 0],
               [1, 1, 0, 1, 0],
               [1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]
    island2 = [[1, 1, 0, 0, 0],
               [1, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 1]]
    i = soln.numDistinctIslands(island1)
    print(i)
    i = soln.numDistinctIslands(island2)
    print(i)

"""
set(['2_0', '2_1', '1_3', '1_1', '1_0', '0_2', '0_3', '0_0', '0_1'])
[set(['2_0', '2_1', '1_3', '1_1', '1_0', '0_2', '0_3', '0_0', '0_1'])]
1

set(['0_1', '1_1', '0_0', '1_0'])
set(['0_0'])
set(['0_0', '0_1'])
[set(['0_1', '1_1', '0_0', '1_0']), set(['0_0']), set(['0_0', '0_1'])]
3

# if res.add(str(st)):
# if res.add(str(st)):
set(['2_0', '2_1', '1_3', '1_1', '1_0', '0_2', '0_3', '0_0', '0_1'])
set(["set(['2_0', '2_1', '1_3', '1_1', '1_0', '0_2', '0_3', '0_0', '0_1'])"])
1

set(['0_1', '1_1', '0_0', '1_0'])
set(['0_0'])
set(['0_0', '0_1'])
set(["set(['0_0'])", "set(['0_1', '1_1', '0_0', '1_0'])", "set(['0_0', '0_1'])"])
3
"""