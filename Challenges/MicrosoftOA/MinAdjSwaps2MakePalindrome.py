"""
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

Practice online: https://www.codechef.com/problems/ENCD12

Example 1:

Input: "mamad"
Output: 3

Example 2:

Input: "asflkj"
Output: -1

Example 3:

Input: "aabb"
Output: 2

Example 4:

Input: "ntiin"
Output: 1
Explanation: swap 't' with 'i' => "nitin"
"""

# Solution 1 :
from collections import defaultdict
from typing import Dict, List


def can_be_palindrome(i: str) -> bool:
    char_count: Dict[str, int] = defaultdict(int)
    for c in i:
        char_count[c] = char_count[c] + 1
    str_len: int = len(i)
    count_odd: int = 0
    for k, e in char_count.items():
        if e % 2 != 0:
            count_odd += 1

    if str_len % 2 == 0:
        return count_odd == 0
    else:
        return count_odd == 1


def compute_palindrome(i: str) -> str:
    char_count: Dict[str, int] = defaultdict(int)
    for c in i:
        char_count[c] = char_count[c] + 1

    res: str = ""
    middle: str = ""
    for c in i:
        if char_count[c] != 0:
            if char_count[c] == 1:
                middle = c
                char_count[c] -= 1
            else:
                res += c
                char_count[c] -= 2

    return res + middle + res[-1::-1]


def min_swaps_anagram(source: str, target: str) -> int:
    s_l: List[str] = list(source)
    t_l: List[str] = list(target)
    count: int = 0
    for i in range(0, len(s_l)):
        pos = s_l[i:].index(t_l[i])

        while 0 < pos:
            s_l[i + pos], s_l[i + pos - 1] = s_l[i + pos - 1], s_l[i + pos]
            count += 1
            pos -= 1

    return count


def min_swaps_palindrome(source: str) -> int:
    if not can_be_palindrome(source):
        return -1

    target = compute_palindrome(source)

    return min_swaps_anagram(source, target)


# Solution 2:
# Simple python solution, O(n^2)
class Solution:
    def minSwap(self, S: str) -> int:
        s = list(S)
        # check if s can be panlindrom
        letter, odd = [0] * 26, 0
        for i in s: letter[ord(i) - ord('a')] += 1
        for l in letter:
            if l & 1 == 1: odd += 1
        if odd > 1: return -1
        i, j, res = 0, len(s) - 1, 0
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
                continue
            t = j - 1
            # find same letter with s[i] from right to left
            while t > i and s[t] != s[i]: t -= 1
            # if t==i, means this is the only letter in the s, should be swap to the middle
            # otherwise should be swap to the position of j
            target = len(s) // 2 if t == i else j
            while t < target:
                # swap
                tmp = s[t]
                s[t] = s[t+1]
                s[t+1] = tmp
                res, t = res + 1, t + 1
        return res
