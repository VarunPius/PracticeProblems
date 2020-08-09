class FirstUnique:
    # def __init__(self, nums: List[int]):
    def __init__(self, nums):
        return

    def showFirstUnique(self) -> int:
        return

    def add(self, value: int) -> None:
        return

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

"""
#########################################################################################################

[Java/Python 3] DoublyLinkedList and LinkedHashSet/dict O(n) 2 neat codes w/ analysis.
Method 1: HashMap + DoublyLinkedList

In order to achieve optimal time performance, we need

    a doubly linked list to keep the order of insertion, and to remove a node corresponding to duplicate numbers and put a node to the end of the list, both in time O(1);
    a hash table to locate the node corresponding to a certain number in amortized time O(1).

In short, the data structure is similar to the one used in LRU Cache, but simpler.


    private static final int mi = Integer.MIN_VALUE, mx = Integer.MAX_VALUE; // dummy values of head and tail.
    private static final DoublyLinkedList head = new DoublyLinkedList(mi),
                                            tail = new DoublyLinkedList(mx);
    private static class DoublyLinkedList {
        
        public DoublyLinkedList prev, next;
        public int val;
        
        public DoublyLinkedList(int v) {
            val = v;
        }
        
    }
    
    private final Map<Integer, DoublyLinkedList> intToNode = new HashMap<>(); // map values to nodes.
    
    public FirstUnique(int[] nums) {
        head.next = tail; // construct empty list: head connects tail.
        tail.prev = head; // construct empty list: tail connects head.
        for (int num : nums) { // add unique numbers to doubly linked list and all entries corresponding to numbers to HashMap.
            add(num);
        }
    }
    
    public int showFirstUnique() {
        return head.next == tail ? -1 : head.next.val; // return -1 if empty list; or the first unique value.
    }

    public void add(int value) {
        DoublyLinkedList node = intToNode.putIfAbsent(value, new DoublyLinkedList(value));
        if (node != null) { // HashMap intToNode already contains entry (value=node).
            remove(node); // value is NOT unique, hence remove it from the doubly linked list.
        }else { // HashMap intToNode does NOT contains key value.
            putToEnd(intToNode.get(value)); // value is unique, hence put it to the end of the doubly linked list.
        }
    }
    
    private boolean remove(DoublyLinkedList node) {
        if (node.prev == null || node.next == null) { // node NOT in the list.
            return false; // remove operation failed.
        }
        node.prev.next = node.next; // modify next pointer of the previous node.
        node.next.prev = node.prev; // modify previous pointer of the next node.
        node.prev = null; // cut off the previous pointer from node to list.
        node.next = null; // cut off the next pointer from node to list.
        return true; // remove operation succeeded.
    }
    
    private boolean putToEnd(DoublyLinkedList node) {
        if (tail == null || tail.prev == null) { // tail node error.
            return false; // operation failed.
        }
        node.next = tail; // assign the tail to the next pointer of node.
        node.prev = tail.prev; // assign the previous node of the tail to the next pointer of node.
        tail.prev = node; // modify previous pointer of the tail.
        node.prev.next = node; // modify next pointer of the previous node.
        return true; // operation succeeded.
    }

class DoublyLinkedList:
    
    def __init__(self, v: int):
        self.prev = self.next = None
        self.val = v

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.intToNode = {}
        self.head, self.tail = map(DoublyLinkedList, (-math.inf, math.inf))
        self.head.next, self.tail.prev = self.tail, self.head
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
      # v = self.head.next.val
      # return -1 if v is math.inf else v
        t = self.head.next
        return -1 if t is self.tail else t.val # credit to discussion between @lmhieu612 and @C0R3 

    def add(self, value: int) -> None:
        if value in self.intToNode:
            self.remove(self.intToNode[value])
        else:
            self.intToNode[value] = DoublyLinkedList(value)
            self.putToEnd(self.intToNode[value])
    def remove(self, node: DoublyLinkedList) -> bool:
        if None in (node.prev, node.next):
            return False
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None
        return True

    def putToEnd(self, node: DoublyLinkedList) -> bool:
        t = self.tail
        if t is None or t.prev is None:
            return False
        node.next, node.prev = t, t.prev
        t.prev, node.prev.next = node, node
        return True

LinkedHashSet can guarantee to keep the order of insertion.

Method 2: HashSet + LinkedHashSet - credit to @CauchyPeano's suggestion.

    private Set<Integer> unique = new LinkedHashSet<>(); 
    private Set<Integer> total = new HashSet<>();
    
    public FirstUnique(int[] nums) {
        for (int n : nums) {
            add(n);
        }
    }
    
    public int showFirstUnique() {
        /*
        for (int v : unique) {
            return v;
        }
        return -1;
        */
        return unique.isEmpty() ? -1 : unique.iterator().next(); // credit to @yelhsabananah
    }
    
    public void add(int value) {
        if (total.add(value)) {
            unique.add(value);
        }else {
            unique.remove(value);
        }
    }

Py3 code - credit to @ZYPHER27 and @easonchan1213 to point out that dict is already ordered in Python 3.6+ and hence OrderedDict is NOT necessary.

    def __init__(self, nums: List[int]):
        self.unique = {}
        self.total = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        '''
        for k in self.unique.keys():
            return k
        return -1
        '''
        return next(iter(self.unique), -1)  # credit to @cwardgar, @C0R3 and @user1633C for contribution of the concise code.
    def add(self, value: int) -> None:
        if value in self.total:
            self.unique.pop(value, 1)
        else:
            self.total.add(value)
            self.unique[value] = 1

Method 3: HashMap + LinkedHashSet

    private Set<Integer> unique = new LinkedHashSet<>(); 
    private Map<Integer, Integer> total = new HashMap<>();
    
    public FirstUnique(int[] nums) {
        for (int n : nums) {
            add(n);
        }
    }
    
    public int showFirstUnique() {
        /*
        for (int v : unique) {
            return v;
        }
        return -1;
        */
        return unique.isEmpty() ? -1 : unique.iterator().next(); // credit to @yelhsabananah
    }
    
    public void add(int value) {
        if (total.containsKey(value)) {
            unique.remove(value);
        }else {
            unique.add(value);
        }
        total.put(value, 1 + total.getOrDefault(value, 0));
    }

Analysis:
Init:
Time & space: O(n), where n = nums.length.

showFirstUnique():
Time & space: O(1)

add():
Time & space: O(1)

#########################################################################################################

[Python 3] OrderedDict + Set, O(1) both operations, O(n) memory
Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted.

Data Structure

    We use an OrderedDict named unique_nums as an ordered hash set to store the unique numbers.
    Only unique numbers will be as a key in unique_nums.
    Then we use a hash set named added_nums to store all numbers ever added so that we can know if a number is added before if it is not in unique_nums.

Analysis

    Time Complexity: O(1) showFirstUnique, O(1) add
    Space Complexity: O(n)

from collections import OrderedDict        

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique_nums = OrderedDict()
        self.added_nums = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # if unique_nums is not empty, return the first key in it. 
        for num in self.unique_nums.keys():
            return num
        return -1

    def add(self, value: int) -> None:
        if value in self.added_nums:
            if value in self.unique_nums:
                del self.unique_nums[value]
        else:
            self.added_nums.add(value)
            self.unique_nums[value] = None # the mapped value doesn't matter
"""