# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def call(slow, fast):
            if slow is None or fast is None:
                return False
            if slow == fast:
                return True
            if fast.next is None:
                return False
            
            return call(slow.next, fast.next.next)

        if head is None or head.next is None or head.next.next is None:
            return False
        return call(head.next, head.next.next)
