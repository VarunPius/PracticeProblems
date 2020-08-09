class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1

        return self.fib(N - 1) + self.fib(N - 2)


"""
naive recursive
def fib(N):
    if N == 0: return 0
    if N == 1: return 1
    return fib(N-1) + fib(N-2)

memoized recursive
memo = {}
def fib(N):
    if N == 0: return 0
    if N == 1: return 1

    if N-1 not in memo: memo[N-1] = fib(N-1)
    if N-2 not in memo: memo[N-2] = fib(N-2)

    return memo[N-1] + memo[N-2]
    
textbook LRU cache
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)
iterative space-optimized

def fib(N):
    if N == 0: return 0
    memo = [0,1]
    for _ in range(2,N+1):
        memo = [memo[-1], memo[-1] + memo[-2]]

    return memo[-1]


can use a tuple for better performance
def fib(N):
    if N == 0: return 0
    memo = (0,1)
    for _ in range(2,N+1):
        memo = (memo[-1], memo[-1] + memo[-2])

    return memo[-1]

or some math
def fib(self, N):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)
"""
