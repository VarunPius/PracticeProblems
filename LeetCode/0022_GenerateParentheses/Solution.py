class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rslt = []
        self.genParenthesisHelper(rslt, "", n, n)
        return rslt

    def genParenthesisHelper(self, rslt, curr, left, right):
        if left == 0 and right == 0:
            rslt.append(curr)
        if left > 0:
            self.genParenthesisHelper(rslt, curr + "(", left - 1, right)
        if left < right:
            self.genParenthesisHelper(rslt, curr + ")", left, right - 1)

if __name__ == '__main__':
    n1 = 3
    n2 = 4
    print(Solution().generateParenthesis(n1))
    print("---")
    print(Solution().generateParenthesis(n2))
