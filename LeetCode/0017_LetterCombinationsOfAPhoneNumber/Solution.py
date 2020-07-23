class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return [""]

        comb, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []

        self.letterCombinationHelper(result, digits, comb, "", 0)
        return result

    def letterCombinationHelper(self, result, digits, comb, curr, idx):
        if len(digits) == len(curr):
            result.append(curr)
        else:
            for i in comb[int(digits[idx])]:
                self.letterCombinationHelper(result, digits, comb, curr + i, idx + 1)


if __name__ == '__main__':
    n1 = "23"
    n2 = "5"
    s = Solution()
    print(s.letterCombinations(n1))
    print(s.letterCombinations(n2))
