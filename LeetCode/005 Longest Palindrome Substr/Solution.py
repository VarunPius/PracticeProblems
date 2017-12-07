class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if (i - maxLen >= 0) and (s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]):
                start = i - maxLen
                maxLen +=1

            if (i - maxLen >= 1) and (s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]):
                start = i - maxLen - 1
                maxLen += 2
        return s[start:start+maxLen]


if __name__ == '__main__':
    s1 = "palindrome"
    s2 = "malayalam"
    sc = Solution()
    print(sc.longestPalindrome(s1))
    print(sc.longestPalindrome(s2))
