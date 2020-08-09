"""
Do not return anything, modify matrix in-place instead.
"""

class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix):
        if not matrix:
            return

        r = len(matrix)
        c = len(matrix[0])
        rowChk = False
        colChk = False

        for i in range(r):
            if matrix[i][0] == 0:
                rowChk = True

        for j in range(c):
            if matrix[0][j] == 0:
                colChk = True

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, r):
            if matrix[i][0] == 0:
                for j in range(1, c):
                    matrix[i][j] = 0

        for j in range(1, c):
            if matrix[0][j] == 0:
                for i in range(1, r):
                    matrix[i][j] = 0

        if rowChk:
            for i in range(r):
                matrix[i][0] = 0

        if colChk:
            for j in range(c):
                matrix[0][j] = 0

