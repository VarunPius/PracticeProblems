class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        return

"""
Assume n % k = r,
we will fill all positions of i with i % k = r,
then the positions with i % k = r - 1,

    def rearrangeString(self, s, k):
        n = len(s)
        if not k: return s
        count = collections.Counter(s)
        maxf = max(count.values())
        if (maxf - 1) * k + count.values().count(maxf) > len(s):
            return ""
        res = list(s)
        i = (n - 1) % k
        for c in sorted(count, key=lambda i: -count[i]):
            for j in range(count[c]):
                res[i] = c
                i += k
                if i >= n:
                    i = (i - 1) % k
        return "".join(res)

"""

"""
Solution 2:
Each heap operation takes constant time since it holds at most 26 elements. So this allows theta(n) time.

class Solution(object):
    def rearrangeString(self, str, k):
        heap = [(-freq, char) 
                for char, freq in collections.Counter(str).items()]
        heapq.heapify(heap)
        res = []
        while len(res) < len(str):
            if not heap: return ""
            freq, char = heapq.heappop(heap)
            stack = []
            res.append(char)
            for j in range(k - 1):
                if len(res) == len(str): return "".join(res)
                if not heap: return ""
                fre, nex = heapq.heappop(heap)
                res.append(nex)
                if fre < -1: 
                    stack.append((fre+1, nex))
            while stack:
                heapq.heappush(heap, stack.pop())
            heapq.heappush(heap, (freq+1, char))
        return "".join(res)

# 56 / 56 test cases passed.
# Status: Accepted
# Runtime: 328 ms
"""

"""
Solution 3:
The idea is simple: we only worry about the most frequent character(s).
For example aaaabbbbcccddefg, ais the most frequent letter, so we start with a structure like
a [] a [] a [] a []
and we just pad other letters in between the a's. Only letters with the same highest frequency can go in to the last []. and we don't care about any letters with lower frequencies, we just scatter them among the paddings. So we end up with
a [bcdf] a [bcdg] a [bce] a [b].
If all the paddings except the last one have length larger than k-1, then we have our answer; else we return ''.

from collections import defaultdict

class Solution(object):
    def rearrangeString(self, string, k):
        if not string:
            return ''

        count = defaultdict(int)
        for s in string:
            count[s] += 1
        # sort the letters according to the frequency
        stack = sorted(list(count.items()), key=lambda t: t[1])

        char, count = stack.pop()  # get most frequent character
        lst = [[char] for _ in range(count)]

        # take care of the letters with same highest freq
        while stack and stack[-1][1] == count:
            char, _ = stack.pop()
            for l in lst:
                l.append(char)

        # all the characters left
        res = ''.join(c*n for c, n in stack)
        # padding
        for i, r in enumerate(res):
            lst[i % (len(lst)-1)].append(r)

        for l in lst[:-1]:
            if len(l) < k:
                return ''

        return ''.join(''.join(l) for l in lst)
"""

"""
Solution 4:
Create a heapq orderd by frequency from big to small. The que length will be at most 26.
Create a cooldown dictionary, key being letter, value being remaining frequency, to hold letters in cool down state.

    If k==0 or k==1, just return s. Otherwise,
    Pop biggest frequency letter from que, add it to result.
    Letter frequency -1, put it to the cool down dictionary.
    For each iteration, pop letter that finished cooling down from the cool down dictionary, push it back to the frequency heap.
    When it is impossible to make a valid result, the result array length must be shorter than input string. In such case we return "".

Time complexity O(nlgm), m is the number of distinct letter. Since k can only be 26, time complexity is O(n)

import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k<=1: 
            return s
        d=collections.defaultdict(int)
        for c in s:
            d[c]+=1
        freqs=[[-d[k],k] for k in d]
        heapq.heapify(freqs)        
        cooling={}
        res=[]
        while freqs:
            freq,c=heapq.heappop(freqs)
            res.append(c)
            freq+=1
            if freq<0:                
                cooling[c]=[freq,c]
            if len(res)>=k and res[-k] in cooling:
                prevFreq,prevC=cooling.pop(res[-k])
                heapq.heappush(freqs,[prevFreq,prevC])        
        return ''.join(res) if len(res)==len(s) else ""
"""