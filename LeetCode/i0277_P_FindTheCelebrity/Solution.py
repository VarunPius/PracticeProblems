# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        return

"""
Solution 1:
def findCelebrity(self, n):
    x = 0
    for i in xrange(n):
        if knows(x, i):
            x = i
    if any(knows(x, i) for i in xrange(x)):
        return -1
    if any(not knows(i, x) for i in xrange(n)):
        return -1
    return x

# 171 / 171 test cases passed.
# Status: Accepted
# Runtime: 1460 ms
# 91.18%

Explanation
# The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
# After the first loop, x is the only candidate.
# The second and third loop is to verify x is actually a celebrity by definition.
# 
# The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison, if a knows b then a < b, if a does not know b, a > b. 
# Then if there is a celebrity, he/she must be the "maximum" of the n people.
# 
# However, the "maximum" may not be the celebrity in the case of no celebrity at all. 
# Thus we need the second and third loop to check if x is actually celebrity by definition.
# 
# The total calls of knows is thus 3n at most. One small improvement is that in the second loop we only need to check i in the range [0, x). 
# You can figure that out yourself easily.
"""

"""
Solution 2:
class Solution(object):
    def findCelebrity(self, n):
        # :type n: int
        # :rtype: int

        # Iterate through each person and find a candidate to be the celebrity

        # The resulting candidate must be a celebrity by the following logic
        # If there is a celebrity, they must
        # a) be known by every person before them (thus, end up as "cand" at some point)
        # b) not know anyone after them (thus, never relinquish "cand")
        cand = 0
        for i in range(n):
            if knows(cand, i):
                cand = i

        # We've established that cand does not know anyone after it
        # Let's establish that cand is known by, but does not know everyone before it
        for i in range (0, cand):
            if knows(cand, i):
                return -1
            if not knows(i, cand):
                return -1
        

        # Last thing we don't know:
        # Does everyone after cand know cand?
        for i in range(cand, n):
            if not knows(i, cand):
                return -1

        return cand
"""

"""
Solution3:
def findCelebrity(self, n):
	# :type n: int
	# :rtype: int
	
	# first, find the candidate for celebrity
	# left and right must meet at some point, this person is a potential celebrity
	left, right = 0, n - 1
	while left < right:
		if knows(left, right):
			left += 1
		else:
			right -= 1

	# next verify if the candidate is indeed a celebrity
	# case 1: at least one person doesn't know this candidate => not a celebrity
	for i in range(n):
		if not knows(i, left) and i != left:
			return -1
	# case2: candidate knows at least one person => not a celebrity
	for i in range(n):
		if knows(left, i) and i != left:
			return -1

	return left
"""