class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s)-1, -2, -1):
            if i == -1 or s[i] != " ":
                break

        for j in range(i, -2, -1):
            if j == -1 or s[j] == " ":
                return i - j


if __name__ == '__main__':
    soln = Solution()
    x = soln.lengthOfLastWord("Hello World")
    print(x)