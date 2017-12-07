class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        copy, reverse = x, 0

        while copy != 0:
            reverse = reverse*10 + copy%10
            copy = copy//10    # 121 = > if single / then results in 12.1,
                               #         but // results in 12

        return x == reverse


if __name__ == "__main__":
    print(Solution().isPalindrome(12))
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(13531))
