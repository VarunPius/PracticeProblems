class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    print("::", string[:i])
                    return string[:i]

        return strs[0]


if __name__ == "__main__":
    str1 = ['hello', "hell", "hi"]
    str2 = ["acv", "acvfg", "acfrth"]
    str3 = []
    sol = Solution()
    print(sol.longestCommonPrefix(str1))
    print(sol.longestCommonPrefix(str2))
    print(sol.longestCommonPrefix(str3))
