import java.util.*;

class Solution {
    public int numDistinctIslands(int[][] grid) {
        if (grid == null || grid.length < 1 || grid[0].length < 1) return 0;
        int m = grid.length, n = grid[0].length;
        Set<String> res = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Set<String> set = new HashSet<>();
                if (grid[i][j] == 1) {
                    dfs(grid, i, j, i, j, set);
                    System.out.println(set);
                    res.add(set.toString());
                }
            }
        }
        System.out.println(res);
        return res.size();
    }

    public void dfs(int[][] grid, int i, int j, int baseX, int baseY, Set<String> set) {
        int m = grid.length, n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) return;
        set.add((i - baseX) + "_" + (j - baseY));
        grid[i][j] = 0;
        dfs(grid, i + 1, j, baseX, baseY, set);
        dfs(grid, i - 1, j, baseX, baseY, set);
        dfs(grid, i, j - 1, baseX, baseY, set);
        dfs(grid, i, j + 1, baseX, baseY, set);
    }

    public static void main(String args[]){
        Solution soln = new Solution();
        int[][] island1 = {{1, 1, 1, 1, 0},
                           {1, 1, 0, 1, 0},
                           {1, 1, 0, 0, 0},
                           {0, 0, 0, 0, 0}};
        int[][] island2 = {{1, 1, 0, 0, 0},
                           {1, 1, 0, 0, 0},
                           {0, 0, 1, 0, 0},
                           {0, 0, 0, 1, 1}};

        System.out.println(soln.numDistinctIslands(island1));
        System.out.println(soln.numDistinctIslands(island2));
    }
}


/*
[0_0, 1_0, 0_1, 2_0, 1_1, 0_2, 2_1, 0_3, 1_3]
[[0_0, 1_0, 0_1, 2_0, 1_1, 0_2, 2_1, 0_3, 1_3]]
1

[0_0, 1_0, 0_1, 1_1]
[0_0]
[0_0, 0_1]
[[0_0, 1_0, 0_1, 1_1], [0_0], [0_0, 0_1]]
3

*/