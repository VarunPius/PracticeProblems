class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []
        result = self.helper(result, matrix)
        final = []
        for i in result:
            final += i
        return final

    def helper(self, result, matrix):
        print("precast line1: ", matrix[0])
        print("list line1: ", list(matrix[0]))
        row = list(matrix.pop(0))
        result.append(row)
        tmp_matrix = list(zip(*matrix))[::-1]    # important as it will return an error; see note
        print("only zip", zip(*matrix))
        print("TM: ", tmp_matrix)
        if matrix:
            self.helper(result, tmp_matrix)
        return result


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    soln = Solution()
    x = soln.spiralOrder(matrix)
    print(x)
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    x = soln.spiralOrder(matrix)
    print(x)

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
    x = soln.spiralOrder(matrix)
    print(x)


"""
Logic:
Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:

    |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    |7 8 9|      |4 7|
Now look at the first rows we extracted:

    |1 2 3|      |6 9|      |8 7|      |4|      |5|

Here's how the zip output looks:
('TM: ', [(8, 12), (7, 11), (6, 10), (5, 9)])
('TM: ', [(11, 10, 9), (7, 6, 5)])
('TM: ', [(5,), (6,), (7,)])
('TM: ', [(6, 7)])
('TM: ', [])
"""
"""
Debug statements matrix 1:
('precast line1: ', [1, 2, 3])
('list line1: ', [1, 2, 3])
('only zip', [(4, 7), (5, 8), (6, 9)])
('TM: ', [(6, 9), (5, 8), (4, 7)])
('precast line1: ', (6, 9))
('list line1: ', [6, 9])
('only zip', [(5, 4), (8, 7)])
('TM: ', [(8, 7), (5, 4)])
('precast line1: ', (8, 7))
('list line1: ', [8, 7])
('only zip', [(5,), (4,)])
('TM: ', [(4,), (5,)])
('precast line1: ', (4,))
('list line1: ', [4])
('only zip', [(5,)])
('TM: ', [(5,)])
('precast line1: ', (5,))
('list line1: ', [5])
('only zip', [])
('TM: ', [])
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

"""
Debug statement matrix 2:
('precast line1: ', [1, 2, 3, 4])
('list line1: ', [1, 2, 3, 4])
('only zip', [(5, 9, 13), (6, 10, 14), (7, 11, 15), (8, 12, 16)])
('TM: ', [(8, 12, 16), (7, 11, 15), (6, 10, 14), (5, 9, 13)])
('precast line1: ', (8, 12, 16))
('list line1: ', [8, 12, 16])
('only zip', [(7, 6, 5), (11, 10, 9), (15, 14, 13)])
('TM: ', [(15, 14, 13), (11, 10, 9), (7, 6, 5)])
('precast line1: ', (15, 14, 13))
('list line1: ', [15, 14, 13])
('only zip', [(11, 7), (10, 6), (9, 5)])
('TM: ', [(9, 5), (10, 6), (11, 7)])
('precast line1: ', (9, 5))
('list line1: ', [9, 5])
('only zip', [(10, 11), (6, 7)])
('TM: ', [(6, 7), (10, 11)])
('precast line1: ', (6, 7))
('list line1: ', [6, 7])
('only zip', [(10,), (11,)])
('TM: ', [(11,), (10,)])
('precast line1: ', (11,))
('list line1: ', [11])
('only zip', [(10,)])
('TM: ', [(10,)])
('precast line1: ', (10,))
('list line1: ', [10])
('only zip', [])
('TM: ', [])
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""

"""
Debug statement matrix 3:
('precast line1: ', [1, 2, 3, 4])
('list line1: ', [1, 2, 3, 4])
('only zip', [(5, 9), (6, 10), (7, 11), (8, 12)])
('TM: ', [(8, 12), (7, 11), (6, 10), (5, 9)])
('precast line1: ', (8, 12))
('list line1: ', [8, 12])
('only zip', [(7, 6, 5), (11, 10, 9)])
('TM: ', [(11, 10, 9), (7, 6, 5)])
('precast line1: ', (11, 10, 9))
('list line1: ', [11, 10, 9])
('only zip', [(7,), (6,), (5,)])
('TM: ', [(5,), (6,), (7,)])
('precast line1: ', (5,))
('list line1: ', [5])
('only zip', [(6, 7)])
('TM: ', [(6, 7)])
('precast line1: ', (6, 7))
('list line1: ', [6, 7])
('only zip', [])
('TM: ', [])
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""

"""
Note:
zip returns an iterable so its important to cast it as list.
also see the boundaries of cast; we are not casting the whole thing but only the zip function
"""
