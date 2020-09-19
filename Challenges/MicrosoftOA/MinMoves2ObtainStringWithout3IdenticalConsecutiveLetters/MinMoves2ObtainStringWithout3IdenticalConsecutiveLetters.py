from itertools import groupby
def minMove(S):
    return sum(len(list(g)) // 3 for _, g in groupby(S))

S = 'baaaaa'
print(minMove(S))

S = 'baaabbaabbba'
print(minMove(S))

S = 'baabab'
print(minMove(S))