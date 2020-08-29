class Solution:
    # def countBattleships(self, board: List[List[str]]) -> int:
    def countBattleships(self, board) -> int:
        if not board: return 0
        m, n = len(board), len(board[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
                    count += 1

        return count
