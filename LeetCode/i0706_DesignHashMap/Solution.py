class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        return

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
I do not think array solutions are acceptable interviews.
So here is my naive implementation of Hash with chaining.
One can play with m (number of slots in HashTable) to optimize the runtime.
I got 90% with setting m = 1000.

# using just arrays, direct access table
# using linked list for chaining

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        ""
        Initialize your data structure here.
        ""
        self.m = 1000;
        self.h = [None]*self.m


    def put(self, key, value):
        ""
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        ""
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)


    def get(self, key):
        ""
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        ""
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

        
    def remove(self, key):
        ""
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        ""
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
"""
