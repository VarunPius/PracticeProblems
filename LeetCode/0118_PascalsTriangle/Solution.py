class Solution:
    # def generate(self, numRows: int) -> List[List[int]]:
    def generate(self, numRows):
        if not numRows or numRows == 0:
            return []
        res = []
        row = [1]
        res.append(row)
        for i in range(numRows - 1):
            row = [x + y for x, y in zip([0] + row, row + [0])]
            res.append(row)
        return res


if __name__ == '__main__':
    soln = Solution()
    i = soln.generate(7)
    print(i)
