# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def call(curr):
            if not curr:
                return 0
            
            res = call(curr.next)
            if res == n:
                curr.next = curr.next.next
            
            return res + 1
        
        res = call(head)
        if res == n: return head.next
    
        return head