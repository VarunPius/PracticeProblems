from collections import defaultdict

class Solution:
    #def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
    def findDiagonalOrder(self, matrix):
        d = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[i + j].append(matrix[i][j])

        ans = []

        for diag in d.items():
            if diag[0] % 2:
                [ans.append(x) for x in diag[1]]
            else:
                [ans.append(x) for x in diag[1][::-1]]

        return ans

if __name__ == '__main__':
    soln = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    x = soln.findDiagonalOrder(matrix)
    print()