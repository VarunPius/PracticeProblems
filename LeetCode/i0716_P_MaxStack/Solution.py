class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        return

    def pop(self) -> int:
        return

    def top(self) -> int:
        return

    def peekMax(self) -> int:
        return

    def popMax(self) -> int:
        return

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

"""
I love implementations that combine a bunch of primitive data structures to make something awesome happen :D

Anyway, I used a heap for efficient finding of the max, and a stack for efficient finding of the most recent.
Each new item was added onto both of these data structures.

I also assigned a decreasing ID to each added value so that they were all uniquely indentifible,
as the same value could be added more than once, and we need to know which were more recently added.
The reason for making them decreasing was so that they could be used to ensure the more recent items came up higher on the heap in the case of ties.

On pop operations, I directly popped from the data structure the operation was on,
and then put the identifier into a set called soft_deleted.
An identifier in soft_deleted represents an item that has been popped from one data structure, but not yet located and removed in the other.
This avoids doing linear searches to try and find items that need deleting.
I noticed a few sample solutions used 2 sets for this purpose, however I don't feel this is necessary.
It's fine for them to share, and with O(1) removal from a set, we're not getting performance gains by separating them.

I defined a private function called _clean_up which checks the tops of the data structures and iteratively removes any soft deleted items from them.
When a soft deleted item is removed, the identifier is also removed from soft_deleted as it no longer needs to be there, due to now being deleted from both sets.

So, we need to ensure that before we do a peek or a pop, that a clean up operation has been run to ensure that the tops of our data structures are clean.
An interesting question is where this should be done.
I decided to do it after a pop, so that then we wouldn't need to call it on peeks, although I need to think more about whether or not this is optimal.
It's important to clean both data structures, because either could be "dirty" from the pop operation.
On the one that had the pop done, the pop might have exposed a soft deleted element.
On the other, it's possible that the element we just popped was also the top on it.

For the rather little test cases given, we can speed it up by not removing stuff from the soft deleted set.
But if we have very large amounts of data going in and out, then in essence it'd be unbounded and thus a nasty memory leak.
For this reason, I think it's better design to be doing those deletes.

Inorder to scale better and reduce memory wastage, we could do a "full clean" whenever the soft deleted set got above a certain size.
This would involve rebuilding the stack and the heap with only the non deleted items.

I'm dubious about this being an easy-level question. Seems much more like a medium to me.

import heapq

class MaxStack:
    def __init__(self):
        self.soft_deleted = set()
        self.max_heap = []
        self.recency_stack = []
        self.next_id = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.recency_stack.append((x, self.next_id))
        self.next_id -= 1

    def _clean_up(self):
        while self.recency_stack and self.recency_stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.recency_stack.pop()[1])
        while self.max_heap and self.max_heap[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.max_heap)[1])

    def pop(self) -> int:
        entry_to_return = self.recency_stack.pop()
        self.soft_deleted.add(entry_to_return[1])
        self._clean_up()
        return entry_to_return[0]

    def top(self) -> int:
        return self.recency_stack[-1][0]

    def peekMax(self) -> int:
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        value, time = heapq.heappop(self.max_heap)
        self.soft_deleted.add(time)
        self._clean_up()
        return value * -1
"""
"""
Solution 2:
from heapq import *

class MaxStack:

    def __init__(self):
        self.ls = []        # list (stack)
        self.hp = []        # heap
        self.hpd = set()    # id of items deleted in ls but not hp
        self.lsd = set()    # id of items deleted in hp but not ls
        self.id = 0

    def push(self, x):
        self.ls.append((self.id, x))
        heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self):
        x = self.top()
        self.hpd.add(self.ls[-1][0])
        self.ls.pop()
        return x

    def top(self):
        while self.ls[-1][0] in self.lsd:
            self.lsd.remove(self.ls[-1][0])
            self.ls.pop()
        return self.ls[-1][1]

    def peekMax(self):
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self):
        x = self.peekMax()
        _, nid = heappop(self.hp)
        self.lsd.add(-nid)
"""
