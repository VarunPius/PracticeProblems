"""
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

Don't include the first or final entry. You can only move either down or right at any point in time.

Example 1:

Input:
[[5, 1],
 [4, 5]]

Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.
Example 2:

Input:
[[1, 2, 3]
 [4, 5, 1]]

Output: 4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
Return the max of that, so 4.
"""


class Solution:
    def sol(self, nums):

        N = len(nums)
        M = len(nums[0])

        nums[0][0] = 1e9
        nums[N - 1][M - 1] = 1e9

        dp = [[1e9] * M for i in range(N)]

        for j in range(1, M):
            dp[0][j] = min(dp[0][j - 1], nums[0][j])
        for i in range(1, N):
            dp[i][0] = min(dp[i - 1][0], nums[i][0])

        for i in range(1, N):
            for j in range(1, M):
                cur = max(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = min(cur, nums[i][j])
        # print(dp)

        print("ans: " + str(dp[N - 1][M - 1]))

def solution(A):
    R = len(A)
    if R == 0:
        return 0
    C = len(A[0])

    for i in range(2, C):
        A[0][i] = min(A[0][i], A[0][i-1])

    for i in range(2, R):
        A[i][0] = min(A[i][0], A[i - 1][0])

    for i in range(1, R):
        for j in range(1, C):
            A[i][j] = max(min(A[i-1][j], A[i][j]),
                          min(A[i][j-1], A[i][j]))

    A[R - 1][C - 1] = max(A[R - 2][C - 1], A[R - 1][C - 2])
    return A[R - 1][C - 1]

"""
Thought process:

Iterate over first row and column. The minimum value must be propagated all the way down the line.
Example:
6, 7, 8
5, 4, 2
8, 7, 6
The top row becomes 6, 6, 6 and the first column becomes 6, 5, 5. Resulting matrix:
6, 6, 6
5, 4, 2
5, 7, 6

Each of the internal elements in the grid will be the minimum of (1) itself, (2) the element above it in the grid, or (3) the element left of it in the grid. Therefore, we want to choose the maximum of two minimum comparisons. Example:
i = 1, j = 1, element = 4.
[i-1, j] = [0, 1] = 6
[i, j-1] = [1, 0] = 5
Therefore, we keep the element 4, since max(min(4, 6), min(4, 5)) == max(4, 4) == 4. For similar reasons, element [1, 2] will remain 2.

Element [2,1], however, will become 5. Note that position [2, 1] can be reached via 6 -> 5 -> 5 -> 7, so we select max(5, 4) and choose 5 as the new element:
i = 2, j = 1, element = 7.
[i-1, j] = [1, 1] = 4
[i, j-1] = [2, 0] = 5
max(min(7, 4), min(7, 5)) == max(4, 5) == 5.
For similar reasons, element [2, 2] will become 5.

We return the value in the bottom right. The answer is 5.

Edit: There is a minor error in this solution, please see the replies to this comment for potential fixes. (We are supposed to ignore the first and last element in the path, which we can achieve with only minor adjustments to this algorithm.)
"""

"""
Java Solution:
private static int maxScore(int[][] grid) {
    int r = grid.length, c = grid[0].length;
    int[][] dp = new int[r][c];
    dp[0][0] = Integer.MAX_VALUE; // first entry is not considered
  
       for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            
            //if its first row and first col, or its first row and second col, or 
            // its second row and first col. Keep the values as it is
            // because we don't have to consider the starting position
            if(i == 0 && j == 0 || i == 0 && j == 1 || i == 1 && j == 0) 
               dp[i][j] = grid[i][j];
            
            else if(i == 0) //if first row (Note : col will be > 1)
                dp[i][j] = Math.min(grid[i][j], grid[i][j - 1]);
            
            else if(j == 0) //if first col (Note : row will be > 1)
                dp[i][j] = Math.min(grid[i][j], grid[i - 1][j]);
            
            //make sure at last row and last col, don't consider its value 
            else if(i == r - 1 && j == c - 1)
                 dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            else
                dp[i][j] = Math.min(grid[i][j], Math.max(dp[i - 1][j], dp[i][j - 1]));
                
        }     
    }
      
      
      return dp[r - 1][c - 1];
  }
"""