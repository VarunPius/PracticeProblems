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


"""
Explanation:
The idea is the following:

d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.
"""