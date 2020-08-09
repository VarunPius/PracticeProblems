class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        return


"""
Intuition

Change the problem to find the LCS

Complexity

Time O(MN) dp,
Space O(MN) * O(string), but actually we can also save the storage of string.

    def shortestCommonSupersequence(self, A, B):
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in xrange(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        res, i, j = "", 0, 0
        for c in lcs(A, B):
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + A[i:] + B[j:]

###############################################################################################
[Java/Python 3] O(mn) clean DP code w/ picture, comments and analysis.
Find LCS;
Let X be “XMJYAUZ” and Y be “MZJAWXU”. The longest common subsequence between X and Y is “MJAU”. The following table shows the lengths of the longest common subsequences between prefixes of X and Y. The ith row and jth column shows the length of the LCS between X_{1..i} and Y_{1..j}.
<lcs.png>
you can refer to here for more details.

Reversely append the chars to StringBuilder, if the char is among the LCS, choose either one between the two strings.
a) start from i = m - 1 and j = n - 1, check if the corresponding chars are equal, that is, s1.charAt(i) == s2.charAt(j); if yes, append either of them; if no, append the char with larger dp value.
b) If we reach left end of s1 or s2 first, continue to append remaining chars in the other string.

    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c in enumerate(s1):
            for j, d in enumerate(s2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i + 1][j], dp[i][j + 1])
        i, j, stk = m - 1, n - 1, []
        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                stk.append(s1[i])
                i -= 1
                j -= 1
            elif dp[i + 1][j] < dp[i][j + 1]:
                stk.append(s1[i])
                i -= 1
            else:
                stk.append(s2[j])
                j -= 1    
        return s1[: i + 1] + s2[: j + 1] + ''.join(reversed(stk))

Analysis:

Time & space:: O(m * n), where m = s1.length(), n = s2.length().

Update:
Q & A

Q: Is it possible to move backwards in the find LCS so you would not need to reverse in the second half?
A:
I believe it is possible, but that will NOT make the code simpler, and there could be more than one solution also.
If you hope to compute dp array backward and construct the common supersequence forward, here is the code:

    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c in reversed(list(enumerate(s1))):
            for j, d in reversed(list(enumerate(s2))):
                dp[i][j] = 1 + dp[i + 1][j + 1] if c == d else max(dp[i + 1][j], dp[i][j + 1])
        i, j, seq = 0, 0, []
        while i < m and j < n:
            if s1[i] == s2[j]:
                seq.append(s1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] > dp[i][j + 1]:
                seq.append(s1[i])
                i += 1
            else:
                seq.append(s2[j])
                j += 1    
        return ''.join(seq) + s1[i :] + s2[j :]

Q: Could you explain the condition being described here? I understand about finishing one string and tacking on the rest of the other. I looked and saw ^ was a bitwise XOR operator, but I didn't understand it in this context.

 if (i < 0 ^ j < 0) { // only one string reaches left end.

A:
Similar to bitwise xor, which results 1 if and only if one operand is 1 and the other is 0: (conditional 1) ^ (conditional 2) is true iff one is true and the other is false. In case you are not comfortable with it, you can rewrite it as:

 if (i < 0 && j >= 0 || j < 0 && i >= 0) { // only one string reaches left end.

end of Q & A

"""
