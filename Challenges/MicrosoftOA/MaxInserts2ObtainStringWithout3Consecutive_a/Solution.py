# Solution 1
def maxInserts(word):
    word = "b"+word+"b"
    idx = [i for i in range(len(word)) if word[i] != "a"]
    count = 0
    for i in range(1,len(idx)):
        diff = idx[i]-idx[i-1]-1
        if diff >= 3:
            return -1
        count+=2-diff
    return count
a = "aabab"
print(maxInserts(a))
a = "dog"
print(maxInserts(a))
a = "aa"
print(maxInserts(a))
a = "baaaa"
print(maxInserts(a))


# Solution 2
from itertools import groupby

def maxInserts1(S):
    ans, last = 0, '#'
    for c, g in groupby(S):
        L = len(list(g))
        if c == 'a':
            if L < 3:
                ans += 2 - L
            else:
                return -1
        else:
            ans += 2 * (L - (last == 'a'))
        last = c
    ans += 2 * (S[-1] != 'a')
    return ans


S = 'aabab'
print(maxInserts(S))

S = 'dog'
print(maxInserts(S))

S = 'aa'
print(maxInserts(S))

S = 'baaaa'
print(maxInserts(S))

# Solution 3
class Solution:
    def max_insert(self, s):
        count = 0
        res = 0

        for c in s:
            if c != 'a':
                res += 2 - count
                count = 0
            else:
                count += 1

            if count == 3:
                return -1
        return res + 2 - count



