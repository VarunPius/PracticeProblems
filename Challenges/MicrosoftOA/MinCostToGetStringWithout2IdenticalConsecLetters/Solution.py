def minCost(s, c):
    i, n = 0, len(s)
    if n < 2:
        return 0

    result = 0
    while i < n:
        localCost = 0
        k = i+1
        localMax = c[i]
        while k < n and s[i] == s[k]:
            localCost += min(localMax, c[k])
            localMax = max(localMax, c[k])
            k += 1
        result += localCost
        i = k
    return result


assert(minCost('abccbd', [0, 1, 2, 3, 4, 5]) == 2)
assert(minCost('a', [9001]) == 0)
assert(minCost('ab', [9001, 9001]) == 0)
assert(minCost('aab', [9001, 1, 9002]) == 1)
assert(minCost('aabbcc', [1, 2, 1, 2, 1, 2]) == 3)
assert(minCost('aaa', [1, 2, 1]) == 2)
assert(minCost('abccccc', [1, 2, 4, 3, 6, 2, 1]) == 10)
print("All passed")

"""
Solution 1:
def solution(S, C):
    total, prev = 0, 0
    for k in range(1, len(S)):
        if S[k - 1] == S[k]:
            total += min(C[k - 1], C[k])
            if C[k - 1] > C[k]:C[k - 1], C[k] = C[k], C[k - 1]
    return total

    
Solution 2:
Simple O(n) python solution

def min_delete_cost(S, C) -> int:
    
    cost = 0
    prev_index = 0
    for i in range(1, len(S)):
        if S[prev_index] == S[i]:
            cost += min(C[prev_index], C[i])
        prev_index += 1
    return cost

assert min_delete_cost('abccbd', [0, 1, 2, 3, 4, 5]) == 2
assert min_delete_cost('aabbcc', [1, 2, 1, 2, 1, 2]) == 3
assert min_delete_cost('aaaa', [3, 4, 5, 6]) == 12
assert min_delete_cost('ababa', [10, 5, 10, 5, 10]) == 0

"""