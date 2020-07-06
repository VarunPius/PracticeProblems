class Solution:
    # def partitionLabels(self, S: str) -> List[int]:
    def partitionLabels(self, S):
        """
        Figure out the rightmost index first and use it to denote the start of the next section.
        Reset the left pointer at the start of each new section.
        Store the difference of right and left pointers + 1 as in the result for each section.

        Rightmost:
        {'a': 8, 'c': 7, 'b': 5, 'e': 15, 'd': 14, 'g': 13, 'f': 11, 'i': 22, 'h': 19, 'k': 20, 'j': 23, 'l': 21}

        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
        a b a b c b a c a d e  f  e  g  d  e  h  i  j  h  k  l  i  j
        """
        rightmost = {c:i for i, c in enumerate(S)}
        print(rightmost)
        left, right = 0, 0
        res = []

        for i, letter in enumerate(S):
            right = max(right, rightmost[letter])

            if i == right:
                res += [right - left + 1]
                left = i + 1
        return res

    def partitionLabels2(self, S):
        res = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            res.append(i)
            S = S[i:]
        return res


if __name__ == '__main__':
    soln = Solution()
    soln.partitionLabels("ababcbacadefegdehijhklij")
