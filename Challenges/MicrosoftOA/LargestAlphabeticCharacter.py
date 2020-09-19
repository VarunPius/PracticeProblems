"""
Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S.
The uppercase character should be returned. For example, for S = "admeDCAB", return "D".
If there is no such character, return "NO".
"""
"""
Python two pass solution using a set.
Time Complexity: O(N)
Space Complexity: O(1) - Since set can only have 26 characters at best
"""


def largestAlphabeticCharacter(s):
    res = ""
    lower_chars = set()

    for c in s:
        if c.islower():
            lower_chars.add(c)
    for c in s:
        if c.isupper() and c.lower() in lower_chars:
            res = max(res, c)

    return res if len(res) > 0 else "NO"

"""
def largest_uppercase_char(S):
    max_upper_char = None
    for c in S:
        if ord("A") <= ord(c) <= ord("Z"):
            if not max_upper_char or ord(c) > ord(max_upper_char):
                max_upper_char = c
    
    if not max_upper_char:
        max_upper_char = "NO"
    return max_upper_char

print(largest_uppercase_char("admeDCAB"))
"""