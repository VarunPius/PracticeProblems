"""
1306
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
"""

def canReach(self, A, i):
    if 0 <= i < len(A) and A[i] >= 0:
        A[i] = -A[i]
        return A[i] == 0 or self.canReach(A, i + A[i]) or self.canReach(A, i - A[i])
    return False

"""
    Check 0 <= i < A.length
    flip the checked number to negative A[i] = -A[i]
    If A[i] == 0, get it and return true
    Continue to check canReach(A, i + A[i]) and canReach(A, i - A[i])

Complexity

Time O(N), as each number will be flipper at most once.
Space O(N) for recursion.
"""