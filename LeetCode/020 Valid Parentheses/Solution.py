class Solution:
    # @return a boolean
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, lookup = [], {"{" : "}", "(" : ")", "[" : "]"}

        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False

        return len(stack) == 0

if __name__ == '__main__':
    paren_set1 = "(){}[]{{{}}}"
    paren_set2 = "[{})"
    print(Solution().isValid(paren_set1))
    print(Solution().isValid(paren_set2))
