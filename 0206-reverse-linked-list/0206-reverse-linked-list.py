# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead = None
        def call(curr, nc):
            if not curr:
                return 

            nonlocal nhead
            ncurr = ListNode(curr.val, nc)
            call(curr.next, ncurr)
            if not nhead:
                nhead = ncurr

        call(head, None)
        return nhead