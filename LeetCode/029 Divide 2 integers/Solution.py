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
