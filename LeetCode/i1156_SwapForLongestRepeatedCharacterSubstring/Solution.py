class Solution:
    def maxRepOpt1(self, text: str) -> int:
        return


"""
Intuition
There are only 2 cases that we need to take care of:

extend the group by 1
merge 2 adjacent groups together, which are separated by only 1 character

Explanation
For S = "AAABBCB"
[[c, len(list(g))] for c, g in groupby(S)] --> [[A,3],[B,2],[C,1],[B,1]]
collections.Counter(S) --> {A:3, B:3, C:1}
With these two data, calculate the best solution for the two cases above.


Complexity
Time O(N)
Space O(N)


Python:
commented by @henry34

    def maxRepOpt1(self, S):
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = collections.Counter(S)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # merge 2 groups together
        for i in xrange(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res

"""
