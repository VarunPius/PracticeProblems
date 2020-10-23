class Solution:
    def gameOfLife(self, board):
        """
        @param board: List[List[int]] = Board representing the cells
                                        1 represents live cell,
                                        0 represents dead cell
        :return: void => we are modifying board in-place.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return

        def find_live_neighbor(board, i, j):
            count = 0
            directions = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], \
                          [i + 1, j - 1], [i + 1, j], [i + 1, j + 1], \
                          [i, j - 1], [i, j + 1]]

            for x, y in directions:
                if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] % 2 == 1:
                    count += 1

            return count

        for j in range(len(board[0])):
            for i in range(len(board)):
                ct_of_live_neighbors = find_live_neighbor(board, i, j)
                if (board[i][j] == 0 and ct_of_live_neighbors == 3) or (
                        board[i][j] == 1 and ct_of_live_neighbors in [2, 3]):
                    board[i][j] |= 2

        for j in range(len(board[0])):
            for i in range(len(board)):
                board[i][j] >>= 1

        return

