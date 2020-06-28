

class Solution:
    #def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    def wordBreak(self, s, wordDict):
        d = [False]*len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or (i-len(w)) == -1):
                    d[i] = True

        return d[-1]


if __name__ == '__main__':
    soln = Solution()
    # x = soln.wordBreak("leetcode", ["leet", "code"])
    x = soln.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print(x)
