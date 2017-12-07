class Solution:
    def myAtoi(self, st):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0

        if not st:
            return result

        i = 0
        sign = 1

        while i < len(st) and st[i].isspace():
            i +=1

        if st[i] == "+":
            i +=1
        elif st[i] == "-":
            i +=1
            sign = -1

        while i < len(st) and '0' <= st[i] <= '9':
            if result > (INT_MAX - int(st[i]))/10:
                return INT_MAX if sign > 0 else INT_MIN

            result = result * 10 + int(st[i])
            i +=1

        return result * sign



if __name__ == '__main__':
    print(Solution().myAtoi(""))
    print(Solution().myAtoi("-1"))
    print(Solution().myAtoi("2147483647"))
    print(Solution().myAtoi("2147483648"))
    print(Solution().myAtoi("-2147483648"))
    print(Solution().myAtoi("-2147483649"))
