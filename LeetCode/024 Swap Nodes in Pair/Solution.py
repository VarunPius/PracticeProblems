class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            next_1, next_2, next_3 = curr.next, curr.next.next, curr.next.next.next
            curr.next = next_2
            next_2.next = next_1
            next_1.next = next_3
            curr = next_1

        return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    print(Solution().swapPairs(head))
