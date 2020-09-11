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
        first = begin.next
        cur = first.next

        while cur != end:
            first.next = cur.next
            cur.next = begin.next
            begin.next = cur
            cur = first.next



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


"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, curr = 0, head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k: return head   # list shorter than k
        new_head, prev = self.reverseList(head, k)
        head.next = self.reverseKGroup(new_head, k)   # the size-k reversed list produced by sefl.reverseList(head, k) reads: prev -> ... -> head
        return prev

    def reverseList(self, head: ListNode, count: int) -> ListNode:
        prev = ListNode(None)
        curr = head
        while count > 0:
            next_node = curr.next   # break curr -> curr.next
            curr.next = prev   # reverse to prev <- curr
            prev = curr   # increment prev node
            curr = next_node   # increment curr node
            count -= 1
        return (curr, prev)   # prev is the head node of the reversed list, the end node of the original list
                              # curr is the head node of the remaining list, since it is the node following prev in the original list
"""