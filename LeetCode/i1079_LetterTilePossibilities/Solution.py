class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def dfs(path, t):
            if path:
                ans.add(path)
            for i in range(len(t)):
                dfs(path + t[i], t[:i] + t[i+1:])
        dfs("", tiles)
        return len(ans)


"""
This is a mathematical problem.
Get the frequencies of different characters [f_0, f_1, ..., f_n].
For each possible choice of frequency [i_0, i_1, ..., i_n] (0 <= i_k <= f_k, k = 0, 1, ..., n),
the number of distinct sequences is (i_0 + i_1 + ... + i_n)! / ( i_0! * i_1! * ... * i_n!).

import collections, math
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = collections.Counter(tiles)
        prod = 1
        for f in freq.values():
            prod *= f + 1
        res = 0
        for i in range(1, prod):
            digits = []
            for f in freq.values():
                digits.append(i % (f + 1))
                i = i // (f + 1)
            tmp = math.factorial(sum(digits))
            for d in digits:
                tmp //= math.factorial(d)
            res += tmp
        return res
"""
