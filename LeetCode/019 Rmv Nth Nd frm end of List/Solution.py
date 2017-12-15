# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next

        while fast.next is not None:    # while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print Solution().removeNthFromEnd(head, 2)
