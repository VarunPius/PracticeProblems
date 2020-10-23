class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        return

    def enqueue(self, element: int) -> None:
        return

    def dequeue(self) -> int:
        return

    def size(self) -> int:
        return


"""
The idea is to use two semaphores, pushing and pulling, to maintain the invariants of the queue.
Initially, no thread can dequeue (self.pulling.acquire()) until a thread has enqueued (self.pulling.release()).
When capacity elements have been enqueued, self.pushing.acquire() will block the thread until a dequeue releases the semaphore again.
Additionally, use a Lock so only a single thread can modify the actual queue at once.

import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
      
        self.queue = collections.deque()

    def enqueue(self, element: int) -> None:
      self.pushing.acquire()
      self.editing.acquire()
      
      self.queue.append(element)
      
      self.editing.release()
      self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        return res

    def size(self) -> int:
      return len(self.queue)
"""

"""
Solution 2:
Simple implementation with 2 locks

from collections import deque
from threading import Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()
        self.q = deque()
        self.capacity = capacity
        self.de.acquire()

    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.q.append(element)
        if len(self.q) < self.capacity:
            self.en.release()
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        val = self.q.popleft()
        if len(self.q):
            self.de.release()
        if val and self.en.locked():
            self.en.release()
        return val
        
    def size(self) -> int:
        return len(self.q)
	

Simple implementation with Condition

from collections import deque
from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.c = Condition()
        self.q = deque()
        self.capacity = capacity

    def enqueue(self, element: int) -> None:
        with self.c:
            self.c.wait_for(lambda: len(self.q) < self.capacity)
            self.q.append(element)
            self.c.notify_all()

    def dequeue(self) -> int:
        with self.c:
            self.c.wait_for(lambda: len(self.q) > 0)
            val = self.q.popleft()
            self.c.notify_all()
            return val
        
    def size(self) -> int:
        return len(self.q)

"""

"""
Solution 3:
simple python solution with 2 semaphores (1 for enqueue and 1 for dequeue)
from threading import Semaphore
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        ""
        :type capacity: int
        ""
        self.c=capacity
        self.l=[]
        self.locks1=Semaphore(self.c) #a total of c spaces at first
        self.locks2=Semaphore(self.c) #a total of 0 element to take at first
        for i in range(0,self.c):
            self.locks2.acquire()
            
    def enqueue(self, element):
        ""
        :type element: int
        :rtype: void
        ""
        self.locks1.acquire()
        self.l.insert(0,element)
        self.locks2.release()

    def dequeue(self):
        ""
        :rtype: int
        ""
        self.locks2.acquire()
        temp=self.l[-1]
        self.l.pop()
        self.locks1.release()
        return temp

    def size(self):
        ""
        :rtype: int
        ""
        return len(self.l)
"""