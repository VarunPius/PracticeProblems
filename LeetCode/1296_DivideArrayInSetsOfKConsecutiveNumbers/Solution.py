from collections import Counter


class Solution:
    # def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    def isPossibleDivide(self, nums, k: int) -> bool:
        c = Counter(nums)
        for i in sorted(c):
            print("Loop")
            if c[i] > 0:
                for j in range(k)[::-1]:
                    print(i, j)
                    print("*", c)
                    c[i+j] -= c[i]
                    print("*#", c)
                    if c[i+j]<0:
                        return False

        return True


if __name__ == '__main__':
    soln = Solution()
    x = soln.isPossibleDivide([1,2,3,3,4,4,5,6], 4)
    print(x)

"""
Solution 1
Count number of different cards to a map c
Loop from the smallest card number.
Everytime we meet a new card i, we cut off i - i + k - 1 from the counter.

Complexity:
Time O(MlogM + MK), where M is the number of different cards.

Debug Print lines:
Loop
1 3
* Counter({3: 2, 4: 2, 1: 1, 2: 1, 5: 1, 6: 1})
*# Counter({3: 2, 1: 1, 2: 1, 4: 1, 5: 1, 6: 1})
1 2
* Counter({3: 2, 1: 1, 2: 1, 4: 1, 5: 1, 6: 1})
*# Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
1 1
* Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
*# Counter({1: 1, 3: 1, 4: 1, 5: 1, 6: 1, 2: 0})
1 0
* Counter({1: 1, 3: 1, 4: 1, 5: 1, 6: 1, 2: 0})
*# Counter({3: 1, 4: 1, 5: 1, 6: 1, 1: 0, 2: 0})
Loop
Loop
3 3
* Counter({3: 1, 4: 1, 5: 1, 6: 1, 1: 0, 2: 0})
*# Counter({3: 1, 4: 1, 5: 1, 1: 0, 2: 0, 6: 0})
3 2
* Counter({3: 1, 4: 1, 5: 1, 1: 0, 2: 0, 6: 0})
*# Counter({3: 1, 4: 1, 1: 0, 2: 0, 5: 0, 6: 0})
3 1
* Counter({3: 1, 4: 1, 1: 0, 2: 0, 5: 0, 6: 0})
*# Counter({3: 1, 1: 0, 2: 0, 4: 0, 5: 0, 6: 0})
3 0
* Counter({3: 1, 1: 0, 2: 0, 4: 0, 5: 0, 6: 0})
*# Counter({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})
Loop
Loop
Loop
True
"""

"""
Solution 2
Count number of different cards to a map c
Cur represent current open straight groups.
In a deque start, we record the number of opened a straight group.
Loop from the smallest card number.
For example, A = [1,2,3,2,3,4], k = 3
We meet one 1:
opened = 0, we open a new straight groups starting at 1, push (1,1) to start.
We meet two 2:
opened = 1, we need open another straight groups starting at 1, push (2,1) to start.
We meet two 3:
opened = 2, it match current opened groups.
We open one group at 1, now we close it. opened = opened - 1 = 1
We meet one 4:
opened = 1, it match current opened groups.
We open one group at 2, now we close it. opened = opened - 1 = 0

return if no more open groups.

Complexity
O(N+MlogM), where M is the number of different cards.
Because I count and sort cards.
In Cpp and Java it's O(NlogM), which can also be improved.

    def isPossibleDivide(self, A, k):
        c = collections.Counter(A)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == k: opened -= start.popleft()
        return opened == 0

"""