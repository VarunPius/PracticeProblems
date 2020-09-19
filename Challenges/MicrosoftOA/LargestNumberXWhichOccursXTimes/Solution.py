"""
Readable Python Solution
Time: O(nlogn)
Space: O(1)
"""

def solve(A):
   if not A: return 0
   A.sort()
   cur = None
   c = 0
   for i in range(len(A) - 1, -1, -1):
       if cur == A[i]: c += 1
       elif cur == None:
           cur = A[i]
           c = 1
       elif c == cur: return cur
       else:
           cur = A[i]
           c = 1
   if c == cur: return cur
   return 0

"""
O(N)

from collections import Counter

def maxCount(a):
  if len(a) == 0:
    return 0
  freq = Counter(a)
  res = 0
  for key, val in freq.items():
    if key == val:
      res = max(res, key)
  return res
"""