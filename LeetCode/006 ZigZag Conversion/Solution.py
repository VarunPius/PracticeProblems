class Solution:
    def convert(self, s, nRows) -> str:
        """
        :type s: str
        :type nRows: int
        :rtype: str
        """
        if nRows == 1 or len(s) < nRows:
            return s

        rslt = ""
        lst = [""]*nRows
        idx = 0
        i = 0

        while i < len(s):
            # print(idx) => 0    Reason we don't need to reset idx to 0 is
            #                      for every itereationthe value will be reset
            while i < len(s) and idx < nRows:
                c = s[i]
                tmp = lst[idx] + c
                lst[idx] = tmp
                i += 1
                idx += 1
            idx = nRows -2

            while i < len(s) and idx > 0:
                c = s[i]
                tmp = lst[idx] + c
                lst[idx] = tmp
                i += 1
                idx -= 1

        rslt = "".join(lst)
        return rslt


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    sc = Solution()
    print(sc.convert(s, 3))
    print(sc.convert(s, 4))
