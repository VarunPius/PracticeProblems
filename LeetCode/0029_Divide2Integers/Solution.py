class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient, dvd, dvs = 0, abs(dividend), abs(divisor)
        sign = (dividend < 0) is (divisor < 0)

        while dvd >= dvs:
            inc = dvs
            i = 0

            while dvd >= inc:
                dvd -= inc
                quotient += 1<<i
                i += 1
                inc<<=1

        if not sign:
            quotient = -quotient

        return min(max(-2147483648, quotient), 2147483647)

    def divide2(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res


# Explanation:
# https://www.youtube.com/watch?v=htX69j1jf5U
