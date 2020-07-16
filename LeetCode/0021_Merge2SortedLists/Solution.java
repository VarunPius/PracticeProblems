/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(0);
        ListNode fnl = ans;
        
        if(l1 == null && l2 == null)
            return null;
            
        if(l1 == null && l2 != null)
            return l2;
        
        if(l2 == null && l1 != null)
            return l1;
        
        while(l1 != null || l2 != null){
            if(l1 == null && l2 != null){
                ans.next = new ListNode(l2.val);
                ans = ans.next;
                l2 = l2.next;
                continue;   //important: else wud give null pointer error in next line
            }
            if(l2 == null && l1 != null){
                ans.next = new ListNode(l1.val);
                ans = ans.next;
                l1 = l1.next;
                continue;       //important: else wud give null pointer error in next line
            }
            if(l1.val < l2.val){
                ans.next = new ListNode(l1.val);
                ans = ans.next;
                l1 = l1.next;
            }
            else if(l1.val == l2.val){
                ans.next = new ListNode(l1.val);
                ans = ans.next;
                ans.next = new ListNode(l2.val);
                ans = ans.next;
                l1 = l1.next;
                l2 = l2.next;
            }
            else if(l1.val > l2.val){
                ans.next = new ListNode(l2.val);
                ans = ans.next;
                l2 = l2.next;
            }
        }
        
        return fnl.next;
    }
}