class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, rowIndex):
        if not rowIndex or rowIndex == 0:
            return [1]
        row = [1]
        for i in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


if __name__ == '__main__':
    soln = Solution()
    i = soln.getRow(3)
    print(i)
