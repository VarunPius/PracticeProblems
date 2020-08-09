class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        row, col = len(matrix), len(matrix[0])
        low = 0
        high = row * col - 1
        while low <= high:
            mid = (low + high)//2
            num = matrix[mid//col][mid%col]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

if __name__ == '__main__':
    soln = Solution()
    print("hello")