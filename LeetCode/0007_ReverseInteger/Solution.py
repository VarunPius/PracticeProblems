class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        rslt = 0
        while x > 0:
            rslt = (rslt*10) + x%10
            x = x//10

        return rslt if rslt <= 0x7FFFFFFF else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        rslt = 0
        if x < 0:
            rslt = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            rslt = int(str(x)[::-1])

        return rslt if abs(rslt) <= 0x7FFFFFFF else 0


if __name__ == '__main__':
    s1 = 123
    s2 = -123456
    sc = Solution()
    print(sc.reverse(s1))
    print(sc.reverse(s2))
    print(sc.reverse2(s1))
    print(sc.reverse2(s2))
