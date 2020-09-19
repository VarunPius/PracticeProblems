# 1375

"""
Explanation

right is the number of the right most lighted bulb.

Iterate the input light A,
update right = max(right, A[i]).

Now we have lighted up i + 1 bulbs,
if right == i + 1,
it means that all the previous bulbs (to the left) are turned on too.
Then we increment res

Complexity

Time O(N)
Space O(1)

"""
def numTimesAllBlue(self, A):
    right = res = 0
    for i, a in enumerate(A, 1):
        right = max(right, a)
        res += right == i
    return res

#1-line Python3
#By @ManuelP
"""
def numTimesAllBlue(self, A):
    return sum(map(operator.eq, itertools.accumulate(A, max), itertools.count(1)))

def numTimesAllBlue(self, A):
    return sum(i == m for i, m in enumerate(itertools.accumulate(A, max), 1))
"""