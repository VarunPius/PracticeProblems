class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = ans = 0
        for i, bulb in enumerate(light, 1):
            right = max(right, bulb)
            ans += right == i
        return ans


"""
i/p: [2,1,3,5,4]

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
