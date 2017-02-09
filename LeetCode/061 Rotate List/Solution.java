/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null)
            return head;

        ListNode fnl = new ListNode(0);
        ListNode last = head;
        fnl.next = head;

        int len = 1;

        while(last.next!=null){
            last = last.next;
            len++;
        }

        int shift = k%len;

        if(shift != 0){
            int lastCoeff = len - shift;
            ListNode prev = null;
            ListNode curr = head;
            for(int i = 0; i<lastCoeff; i++){
                prev = curr;
                curr = curr.next;
            }

            last.next = head;
            prev.next = null;
            head = curr;
            fnl.next = head;
        }

        return fnl.next;
    }
}
