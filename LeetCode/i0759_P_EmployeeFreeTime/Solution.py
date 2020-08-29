"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        return


"""
Solution 1:
Key points:
- recognize that this is very similar to merging intervals (https://leetcode.com/problems/merge-intervals/description/)
- it doesn't matter which employee an interval belongs to, so just flatten
- can build result array while merging, don't have to do afterward (and don't need full merged arr)

def employeeFreeTime(self, schedule):
    ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
    res, pre = [], ints[0]
    for i in ints[1:]:
        if i.start <= pre.end and i.end > pre.end:
            pre.end = i.end
        elif i.start > pre.end:
            res.append(Interval(pre.end, i.start))
            pre = i
    return res
"""

"""
Solution 2:
The idea is to sort all the intervals based on the starting time. this gives a set of busy intervals. After merging all the busy times, the gaps in between, form the free time common to everyone in the list.
Using a stack, we can start merging the intervals, and whenever a new interval is pushed to the stack, the time between the last seen interval and the new interval is a free time that can be added to the result.

def employeeFreeTime(self, avails):
    avails = list(sorted(chain(*avails), key=lambda interval: interval.start))
    stack = [avails[0]]
    res = list()
    for cur in avails[1:]:
        top = stack.pop()
        if top.end < cur.start:
            res.append(Interval(top.end, cur.start))
            stack.append(cur)
        else:
            if cur.end <= top.end:
                stack.append(top)
            else:
                stack.append(cur)
    return res
"""