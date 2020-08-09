# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev

    # Recursive
    def reverseList2(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev = None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)


