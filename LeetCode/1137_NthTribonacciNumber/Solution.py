class Solution:
    def tribonacci(self, n: int) -> int:
        x, y, z = 1, 0, 0
        for _ in range(n):
            x, y, z = y, z, x + y + z
        return z
