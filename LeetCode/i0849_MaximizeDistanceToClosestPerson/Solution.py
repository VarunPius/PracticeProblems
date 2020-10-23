class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        return


"""
Explanation
last is the index of last seated seat.
Loop on all seats, when we met a people, we count the distance from the last.
The final result = max(distance at the beginning, distance in the middle / 2, distance at the end).

Explanation
Time O(N) Space O(1)

    def maxDistToClosest(self, seats):
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) / 2)
                last = i
        return max(res, n - last - 1)

"""
