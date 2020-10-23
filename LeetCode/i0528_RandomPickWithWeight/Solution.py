class Solution:

    def __init__(self, w: List[int]):
        return

    def pickIndex(self) -> int:
        return

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

"""
The problem is, we need to randomly pick an index proportional to its weight.
What this means? 
We have weights array, each
weights[i]  represents weight of index i. 
The more the weight is, then high chances of getting that index randomly.

suppose weights = [1, 3]
then 3 is larger, so there are high chances to get index 1.

We can know the chances of selecting each index by knowing their probability.

P(i) = weight[i]/totalWeight

totalWeight = 1 + 3 = 4
So, for index 0, P(0) = 1/4  = 0.25 = 25%
for index 1, P(1) = 3/4 = 0.75 = 75%

So, there are 25% of chances to pick index 0 and 75% chances to pick index 1.

"""

"""
class Solution:

    def __init__(self, w):
        ""
        :type w: List[int]
        ""
        self.w = w
        self.n = len(w)
        for i in range(1,self.n):
            w[i] += w[i-1]
		self.s = self.w[-1]

    def pickIndex(self):
        ""
        :rtype: int
        ""
        seed = random.randint(1,self.s)
        l,r = 0, self.n-1
        while l<r:
            mid = (l+r)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l

"""

"""

"""