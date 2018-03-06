class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not (self.isValid([board[i][j] for j in range(9)]) and \
                    self.isValid([board[j][i] for j in range(9)])):
                return False

        for i in range(3):
            for j in range(3):
                if not self.isValid([board[m][n] for n in range(3*j, 3*j+3) \
                    for m in range(3*i, 3*i+3)]):
                    return False
        return True

    def isValid(self, xs):
        xs = list(filter(lambda x : x != ".", xs))
        # list(filter ...) because only filter will return filter object
        #   that needs to be used with iterable object or generator
        return len(set(xs)) == len(xs)

if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    board1 =[[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    print(Solution().isValidSudoku(board))
    print(Solution().isValidSudoku(board1))
