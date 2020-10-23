class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1:i]) <= 9:    # >0 and not >= 0 ; see note2
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


"""
Note 1:
This is my first post. Please let me know if this is helpful and if there's anything I can do to improve.

Problem Reduction: variation of n-th staircase with n = [1, 2] steps.

Approach: We generate a bottom up DP table.

The tricky part is handling the corner cases (e.g. s = "30").

Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].

Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

For example:
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2


Note2:
Will fail for something like "10" where it will add an extra 1 for 0 and result in extra way
"""
