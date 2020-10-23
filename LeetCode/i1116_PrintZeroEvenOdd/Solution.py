class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        return

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        return

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        return

"""
from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroSem = Semaphore() # default is 1.
        self.oddSem = Semaphore(0)       
        self.evenSem = Semaphore(0)       
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zeroSem.acquire()
            printNumber(0)
            (self.evenSem if i % 2 else self.oddSem).release()  # Alternately release oddSem and evenSem.   
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.evenSem.acquire()
            printNumber(i)
            self.zeroSem.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddSem.acquire()
            printNumber(i)
            self.zeroSem.release()
"""
"""
from threading import Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sem = 0
        self.c = Condition()       
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.c:
                while self.sem: self.c.wait()
                printNumber(0)
                self.sem = 2 if i % 2 else 1  # Alternately turn to odd() and even().   
                self.c.notify_all()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            with self.c:
                while self.sem - 2: self.c.wait()
                printNumber(i)
                self.sem = 0
                self.c.notify_all()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            with self.c:
                while self.sem - 1: self.c.wait()
                printNumber(i)
                self.sem = 0
                self.c.notify_all()
"""