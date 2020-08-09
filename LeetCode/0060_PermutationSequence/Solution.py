import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = ''
        numbers = [i for i in range(1, n + 1)]
        k -=1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation


if __name__ == '__main__':
    soln = Solution()
    x = soln.getPermutation(4, 9)
    print(x)
