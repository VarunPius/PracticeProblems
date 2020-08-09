class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        return

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        return

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

"""
Record the number of moves for each rows, columns, and two diagonals.
For each move, we -1 for each player 1's move and +1 for player 2's move.
Then we just need to check whether any of the recored numbers equal to n or -n.

class TicTacToe(object):

    def __init__(self, n):
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n
        
    def move(self, row, col, player):
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0

Let's only look at rows first:
row[] represents the move count of a row
If player1 move on a cell in row[1], then row[1]+=1
If player2 move on a cell in row[1], then row[1]-=1
If both player1 and player2 move on some cells in row[1], then row[1] will never become "n" because it is guaranteed that all moves are valid and will only moves on empty cells.
If row[1] becomes "n", if it is currently player1's move, then player1 wins, else player2 wins.
For each move, only check rows of current move, no need to check all rows.

Do the same for columns to check winning condition on column.

For diagnal, if rowIdx-colIdx==0, that means the move is on top-left to right-bottom diagnal. If rowIdx+colIdx==n, that means the move is on top-right to bottom-left diagnal.

So total space is "rows array + columns array + two diagnals": O(n+n+1+1)==O(n)
For each move, time checking current row, column, and two diagnals takes O(1+1+1+1)==O(1)

class TicTacToe:
    def __init__(self, n: int):
        self.row=[0]*n
        self.col=[0]*n
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row]+=1 if player==1 else -1
        self.col[col]+=1 if player==1 else -1
        if row+col==self.n-1:
            self.diag1+=1 if player==1 else -1
        if row-col==0:
            self.diag2+=1 if player==1 else -1
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
            return 1 if player==1 else 2
        return 0

"""