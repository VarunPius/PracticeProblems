class Solution:
    # O(m*n) space
    #def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for x in range(c)] for x in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i - 1][0]*(1 - obstacleGrid[i][0])
        for j in range(1, c):
            dp[0][j] = dp[0][j - 1]*(1 - obstacleGrid[0][j])

        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])*(1 - obstacleGrid[i][j])

        return dp[-1][-1]

"""
# O(n) space
def uniquePathsWithObstacles2(self, obstacleGrid):
    if not obstacleGrid:
        return 
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    cur = [0] * c
    cur[0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, c):
        cur[i] = cur[i-1] * (1 - obstacleGrid[0][i])
    for i in xrange(1, r):
        cur[0] *= (1 - obstacleGrid[i][0])
        for j in xrange(1, c):
            cur[j] = (cur[j-1] + cur[j]) * (1 - obstacleGrid[i][j])
    return cur[-1]

# in place
def uniquePathsWithObstacles(self, obstacleGrid):
    if not obstacleGrid:
        return 
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, r):
        obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
    for i in xrange(1, c):
        obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
    for i in xrange(1, r):
        for j in xrange(1, c):
            obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
    return obstacleGrid[-1][-1]
    """