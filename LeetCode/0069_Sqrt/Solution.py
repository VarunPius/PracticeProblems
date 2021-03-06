class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1

"""
This is newton's method. 
Shorter version:
    r = x
    while r*r > x:
        r = (r + x/r) / 2
    return r

Slight alterations:
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid
"""