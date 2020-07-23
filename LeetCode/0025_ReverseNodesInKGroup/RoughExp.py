class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or k < 2:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        cur, cur_dummy = head, dummy
        length = 0

        while cur:
            next_cur = cur.next
            length = (length + 1)%k
            #print("Lenght: ", length, "cur: ", next_cur.val)

            if length == 0:
                nxt_dummy = cur_dummy.next
                self.reverse(cur_dummy, next_cur)
                cur_dummy = nxt_dummy
            cur = next_cur

        return dummy.next


    def reverse(self, begin, end):
        first = None
        cur = begin.next
        #print("Val: ", cur.val)
        if cur:
            nxt = cur.next
        else:
            return

        while cur != end and cur is not None:
            cur.next = first
            first = cur
            cur = nxt
            if nxt:
                nxt = nxt.next



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    #print(Solution().reverseKGroup(head, 2))
    print(Solution().reverseKGroup(head, 3))
