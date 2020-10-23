class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return


"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        ""
        :type s: str
        :rtype: int
        ""
        left, longest, d = 0, 0, {}
        maximum_distinct = 2
        for index, char in list(enumerate(s)):
            d[char] = index
            if len(d.keys()) == maximum_distinct + 1:
                index_to_remove = min([d[char] for char in d.keys()])
                d.pop(s[index_to_remove], None)
                left = index_to_remove + 1
            longest = max(longest, index - left + 1)
        return longest
"""