class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        i, idx = 0, 1

        while idx < len(A):
            if A[i] != A[idx]:
                i += 1
                A[i] = A[idx]

            idx += 1

        return i + 1
