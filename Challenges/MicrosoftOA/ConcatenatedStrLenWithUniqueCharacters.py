"""
Given an Array A consisting of N Strings, calculate the length of the longest string S such that:

    S is a concatenation of some of the Strings from A.
    every letter in S is different.

Example -
A = ["co","dil","ity"] , function should return 5, resulting string S could be codil , dilco, coity,ityco
A = ["abc","kkk","def","csv"] , returns 6 , resulting Strings S could be abcdef , defabc, defcsv , csvdef
A = ["abc","ade","akl"] , return 0 , impossible to concatenate as letters wont be unique.

N is [1..8] ; A consists of lowercase English letters ; sum of length of strings in A does not exceed 100.
"""


def get_max_len(arr):
    # start with unique elements in given list
    dp = [set(x) for x in arr if len(set(x)) == len(x)]

    for v in arr:
        # check for duplicates
        if len(a := set(v)) == len(v):
            # concat to each valid set in list
            for b in dp:
                # skip if sets share letters
                if a & b:
                    continue
                # combine sets, add to dp
                dp.append(a | b)
    # remove initial sets because we need to concatenate
    for x in arr:
        if (tmp := set(x)) in dp:
            dp.remove(tmp)
    # make sure we have valid answer
    return max(len(x) for x in dp) if dp else 0


assert get_max_len(["co", "dil", "ity"]) == 5
assert get_max_len(["abc", "kkk", "def", "csv"]) == 6
assert get_max_len(["abc", "ade", "akl"]) == 0
assert get_max_len(["abdfc", "xjk", "akl"]) == 8
assert get_max_len(["ab", "dfc", "xjk", "akl"]) == 8
assert get_max_len(["abdfc", "xjk", "zhu"]) == 11
assert get_max_len(["ab", "d", "fc", "xj", "k", "zhu"]) == 11
assert get_max_len(["ab", "dfc", "xjk", "zh", "u"]) == 11
assert get_max_len(["abc", "dfcy", "xjk", "zh", "u"]) == 10
assert get_max_len(["abc", "dfc", "xjk", "zh", "u"]) == 9

# leetcode 1239:
def maxLength(self, A):
    dp = [set()]
    for a in A:
        if len(set(a)) < len(a): continue
        a = set(a)
        for c in dp[:]:
            if a & c: continue
            dp.append(a | c)
    return max(len(a) for a in dp)