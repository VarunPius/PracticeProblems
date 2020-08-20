"""
Zombie Matrix
Hard

Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?

Example:
Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]

int minHours(int rows, int columns, List<List<Integer>> grid) {
	// todo
}
"""


class Solution:
    def humanDays(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])

        q = [[i, j] for i in range(row) for j in range(col) if matrix[i][j] == 1]
        time = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while True:
            new = []
            for coor in q:
                for d in direction:
                    ni, nj = coor[0] + d[0], coor[1] + d[1]
                    if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == 0:
                        matrix[ni][nj] = 1
                        new.append([ni, nj])

            q = new
            if not q:
                break

            time += 1

        return time


if __name__ == '__main__':
    soln = Solution()
    i = soln.humanDays([[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]])
    print(i)
