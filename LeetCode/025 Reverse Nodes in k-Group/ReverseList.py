class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

    @staticmethod
    def displayList(hd):
        while hd:
            print("Node: ", hd.val)
            hd = hd.next


class Solution:
    def reverseMain(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        hd = self.reverse(dummy)
        return hd


    def reverse(self, begin):
        first = None
        cur = begin.next
        nxt = cur.next

        while cur:
            cur.next = first
            first = cur
            cur = nxt
            if nxt:
                nxt = nxt.next

        print("First and Last Values: ", begin.val, first.val)
        return first


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
    hd = Solution().reverseMain(head)
    ListNode.displayList(hd)
