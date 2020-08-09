# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if head.next is None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1
        rotateLen = k%length
        if rotateLen == 0 or k == 0:
            return head

        fastPointer = head
        slowPointer = head

        for _ in range(rotateLen):
            fastPointer = fastPointer.next

        while fastPointer.next:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next

        temp = slowPointer.next
        slowPointer.next = None
        fastPointer.next = head
        head = temp
        return head
