class Solution:
    # def minTotalDistance(self, grid: List[List[int]]) -> int:
    def minTotalDistance(self, grid) -> int:
        return


"""
Solution 1:
Before solving the 2D problem we first consider a 1D case. The solution is quite simple. Just find the median of all the x coordinates and calculate the distance to the median.

Alternatively, we can also use two pointers to solve the 1D problem. left and right are how many people one left/right side of coordinates i/j. If we have more people on the left we let j decrease otherwise increase i. The time complexity is O(n) and space is O(1).

To be more clear, a better view is we can think i and j as two meet points. All the people in [0, i] go to meet at i and all the people in [j, n - 1] meet at j. We let left = sum(vec[:i+1]), right = sum(vec[j:]), which are the number of people at each meet point, and d is the total distance for the left people meet at i and right people meet at j.

Our job is to let i == j with minimum d.

If we increase i by 1, the distance will increase by left since there are 'left' people at i and they just move 1 step. The same applies to j, when decrease j by 1, the distance will increase by right. To make sure the total distance d is minimized we certainly want to move the point with less people. And to make sure we do not skip any possible meet point options we need to move one by one.

For the 2D cases we first need to sum the columns and rows into two vectors and call the 1D algorithm.
The answer is the sum of the two. The time is then O(mn) and extra space is O(m+n)

Moreover, the solution is still O(mn) with the follow up:
    What if there are people sharing same home?
    In other words the number in the grid can be more than 1.

def minTotalDistance(self, grid):
    row_sum = map(sum, grid)
    col_sum = map(sum, zip(*grid)) # syntax sugar learned from stefan :-)

    def minTotalDistance1D(vec):
        i, j = -1, len(vec)
        d = left = right = 0
        while i != j:
            if left < right:
                d += left
                i += 1
                left += vec[i]
            else:
                d += right
                j -= 1
                right += vec[j]
        return d

    return minTotalDistance1D(row_sum) + minTotalDistance1D(col_sum)

# 57 / 57 test cases passed.
# Status: Accepted
# Runtime: 40 ms
"""

"""
Solution 2:
def minTotalDistance(self, grid):
    if not grid:
        return 0
    r, c = len(grid), len(grid[0])
    sumr = [i for i in xrange(r) for j in xrange(c) if grid[i][j]]
    sumc = [j for i in xrange(r) for j in xrange(c) if grid[i][j]]
    sumr.sort()
    sumc.sort()
    mid_row = sumr[len(sumr)/2]
    mid_col = sumc[len(sumc)/2]
    return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])
"""
