# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1, ll2 = 0, 0
        c1 = l1
        while c1:
            c1 = c1.next
            ll1 += 1
        
        c2 = l2
        while c2:
            c2 = c2.next
            ll2 += 1
        
        while ll1 < ll2:
            l1 = ListNode(0, l1)
            ll1 += 1
        
        while ll2 < ll1:
            l2 = ListNode(0, l2)
            ll2 += 1
        
        def call(c1, c2):
            if c1:
                res, c = call(c1.next, c2.next)
                res = ListNode((c1.val + c2.val + c) % 10, res)
                c = (c1.val + c2.val + c) // 10
                return res, c
            return None, 0
        
        res, c = call(l1, l2)
        if c:
            res = ListNode(c, res)
        return res