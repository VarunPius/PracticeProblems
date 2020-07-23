class Solution(object):
    # def countAndSay(self, n: int) -> str:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n - 1):
            count = 1
            tmp = []

            for idx in range(1, len(s)):
                if s[idx] == s[idx - 1]:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(s[idx - 1])
                    count = 1
            tmp.append(str(count))
            tmp.append(s[-1])
            s = "".join(tmp)
        return s
