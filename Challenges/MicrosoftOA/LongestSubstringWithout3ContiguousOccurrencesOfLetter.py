"""
Given a string s containing only a and b, find longest substring of s such that s does not contain more than two contiguous occurrences of a and b.

Example 1:

Input: "aabbaaaaabb"
Output: "aabbaa"

Example 2:

Input: "aabbaabbaabbaa"
Output: "aabbaabbaabbaa"

"""

from itertools import groupby
def longestWithout3(S):
    loc, ans = '', ''
    for c, g in groupby(S):
        glen = len(list(g))
        ans = max([ans, loc + c * min(glen, 2)], key=len)
        if glen > 2:
            loc = c*2
        else:
            loc += c*glen
    return ans

assert longestWithout3("aabbaaaaabb") == "aabbaa"
assert longestWithout3("aabbaaaaabbaabbaabbaabbab") == "aabbaabbaabbaabbab"
assert longestWithout3("aabbaabbaabbaa") == "aabbaabbaabbaa"
assert longestWithout3("aaabb") == "aabb"

print("all tests passed")