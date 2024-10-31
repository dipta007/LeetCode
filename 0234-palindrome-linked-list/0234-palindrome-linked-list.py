# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head

        def call(curr):
            if not curr:
                return True

            if not call(curr.next):
                return False
            
            nonlocal tmp
            if tmp.val != curr.val:
                return False
            
            tmp = tmp.next

            return True
        
        return call(head)
