/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null)
            return head;
        
        ListNode fast = head;
        ListNode tmp = new ListNode(0);
        tmp.next = head;
        
        while(n>0){
            if(fast == null)
                fast = head;
            fast = fast.next;
            n--;
        }
        
        ListNode curr = tmp;
        while (fast != null){
            fast = fast.next;
            curr = curr.next;
        }
        curr.next = curr.next.next;
        
        return tmp.next;
        
    }
}