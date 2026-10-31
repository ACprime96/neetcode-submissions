/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1);
        ListNode head = dummy;
        ListNode l1 = list1, l2 = list2;
        while(l1 != null && l2 != null) {
            ListNode temp = new ListNode(-1);
            if(l1.val < l2.val) {
                temp.val = l1.val;
                l1 = l1.next;
            }
            else {
                temp.val = l2.val;
                l2 = l2.next;
            }
            dummy.next = temp;
            dummy = dummy.next;
        }
        while(l1 != null) {
            ListNode temp = new ListNode(l1.val);
            dummy.next = temp;
            dummy = dummy.next;
            l1 = l1.next;
        }

        while(l2 != null) {
            ListNode temp = new ListNode(l2.val);
            dummy.next = temp;
            dummy = dummy.next;
            l2 = l2.next;
        }
        return head.next;
    }
}