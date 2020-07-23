/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode tmp = new ListNode(0);
        ListNode fnl = tmp;
        tmp.next = head;
        
        while(tmp.next != null && tmp.next.next != null){
            ListNode first = tmp.next;
            ListNode second = tmp.next.next;
            
            first.next = second.next;
            tmp.next = second;
            tmp.next.next = first;
            
            tmp = tmp.next.next;
        }
        
        return fnl.next;
    }
}