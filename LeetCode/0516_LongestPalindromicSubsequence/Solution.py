class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n-1]

"""
Above solution is O(n^2) space: accepted in ~900 ms

Alternate solution:
This space O(n) DP solution got accepted in 619 ms, beating 100%.

    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in xrange(n)]
        dp[n-1] = 1

        for i in xrange(n-1, -1, -1):   # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
                    
        return dp[n-1]

"""