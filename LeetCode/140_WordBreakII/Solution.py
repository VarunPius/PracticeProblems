class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    def __init__(self):
        self.result = []

    def wordBreak(self, s, wordDict):
        if not s:
            return [""]
        wordDict = set(wordDict)
        dp = self.dp(s, wordDict)
        self.dfs(s, "", 0, wordDict, dp)

        return self.result

    def dp(self, s, wordDict):
        N = len(s)
        dp = [False] * (N+1)
        dp[0] = True
        for i in range(N):
            for j in range(i, N+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp

    def dfs(self, s, path, idx, wordDict, dp):
        if dp[idx + len(s)]:
            if not s:
                self.result.append(path.strip())

            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], path + " " + s[:i], idx + i, wordDict, dp)

