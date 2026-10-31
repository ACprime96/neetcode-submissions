# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == head:
            return True
        if not head.next:
            return False
        s, f = head, head
        while f:
            s = s.next
            f = f.next
            f = f.next if f else f
            if s == f:
                return True
        return False
        