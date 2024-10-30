# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        head = ListNode()
        curr = head
        c1, c2 = l1, l2
        while c1 and c2:
            s = c1.val + c2.val + c
            curr.next = ListNode(s % 10)
            curr = curr.next
            c = s // 10

            c1 = c1.next
            c2 = c2.next
        
        while c1:
            s = c1.val + c
            curr.next = ListNode(s % 10)
            curr = curr.next
            c1 = c1.next
            c = s // 10

        while c2:
            s = c2.val + c
            curr.next = ListNode(s % 10)
            curr = curr.next
            c2 = c2.next
            c = s // 10
        
        if c:
            curr.next = ListNode(c % 10)
        
        return head.next