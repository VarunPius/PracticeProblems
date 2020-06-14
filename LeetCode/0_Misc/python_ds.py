# Deque:
from collections import deque

q = deque([1, 2, 3, 4, 5]) # Notice the parenthesis syntax
print(q)
# deque([1, 2, 3, 4, 5])

# Deque functions:
# - append(<val>): Insert the value to the right end of deque
# - appendleft(<val>): Insert the value to the left end of deque
# - pop():  delete an argument from the right end of deque.
# - popleft():  delete an argument from the left end of deque.

q.append(6)
q.append("a")
q.appendleft([6, 7, 8])
print(q)
# deque([[6, 7, 8], 1, 2, 3, 4, 5, 6, 'a'])

x = q.pop()
y = q.popleft()
print(x, y, q)
# ('a', [6, 7, 8], deque([1, 2, 3, 4, 5, 6]))

# - index(ele, beg, end) : returns the 1st idx of the val mentioned in arguments, starting search from beg till end idx
# - insert(i, a) : inserts the value mentioned in arguments(a) at index(i) specified in arguments
# - remove(<val>) : removes the first occurrence of value mentioned in arguments
# - count(<val>) : counts the number of occurrences of value mentioned in arguments
try:
    x = q.index(6, 1, 4)
    print(x)
except Exception as err:   # can be written as `except ValueError as err:` if you know the error
    print(err)
# 6 is not in deque

x = q.index(6, 1)
print(x)
# 5
q.insert(2, 7)
q.remove(5)
y = q.count(2)
print(q, y)
# deque([1, 2, 7, 3, 4, 6]) 1




