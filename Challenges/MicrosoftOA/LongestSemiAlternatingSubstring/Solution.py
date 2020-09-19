"""
A brief summary of two problems:

    Longest Substring Without 2 Contiguous Occurrences of Letter: https://leetcode.com/discuss/interview-question/398031/
    Longest Semi-Alternating Substring: https://leetcode.com/discuss/interview-question/398037/

Based on my observation:
substring without 2 contiguous occurrences of letter (a substring does not contain more than two contiguous occurrences)
semi-alternating substring (a substring does not contain 3 identical consecutive chars)

Semantically, they are the same problems. However, the 1st question is asking for a substring, and the 2nd question is asking for the length of the substring.

"""


# solution to the 1st problem
def longestSubstr2(s):
    if len(s) < 3:
        return s

    cur = 0
    start = 0  # anchor pointer (expected to be the start idx of the substring)
    end = 1  # look-ahead pointer
    ch = s[0]
    count = 1  # count the occurance of the first char
    max_len = 1

    while end < len(s):
        if s[end] == ch:
            count += 1

            if count == 2:
                if end - cur + 1 > max_len:
                    max_len = end - cur + 1
                    start = cur  # set anchor pointer if length is max

            elif count > 2:
                cur = end - 1  # reset cur pointer

        else:
            ch = s[end]
            count = 1

            if end - cur + 1 > max_len:
                max_len = end - cur + 1
                start = cur

        end += 1

    return s[start: start + max_len]


# solution to the 2nd problem
def longestSemiAlterSubstr(s):
    if not s or len(s) == 0:
        return 0

    if len(s) < 3:
        return len(s)

    cur = 0
    end = 1  # look-ahead pointer
    ch = s[0]
    count = 1  # count the occurance of the first char
    max_len = 1

    while end < len(s):
        if s[end] == ch:
            count += 1

            if count == 2:
                if end - cur + 1 > max_len:
                    max_len = end - cur + 1

            elif count > 2:
                cur = end - 1  # reset cur pointer

        else:
            ch = s[end]
            count = 1

            if end - cur + 1 > max_len:
                max_len = end - cur + 1

        end += 1

    return max_len
