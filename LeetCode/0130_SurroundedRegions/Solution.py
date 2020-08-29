from itertools import product


class Solution:
    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= self.M or j >= self.N or self.board[i][j] != "O":
            return
        self.board[i][j] = "T"
        traverse_list = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
        for x, y in traverse_list:
            self.dfs(x, y)

    # def solve(self, board: List[List[str]]) -> None:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 0

        self.board, self.M, self.N = board, len(board), len(board[0])

        for i in range(self.M):
            self.dfs(i, 0)
            self.dfs(i, self.N - 1)

        for j in range(self.N):
            self.dfs(0, j)
            self.dfs(self.M - 1, j)

        for i, j in product(range(self.M), range(self.N)):
            self.board[i][j] = "X" if self.board[i][j] != "T" else "O"


