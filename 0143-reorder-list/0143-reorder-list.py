# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the median
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the list from mid
        prev, curr = None, slow
        while curr:
            tmp = curr.next

            curr.next = prev
            prev = curr
            curr = tmp
        
        # merge
        c1, c2 = head, prev
        while c2.next:
            tmp1 = c1.next
            c1.next = c2
            
            tmp2 = c2.next
            c2.next = tmp1

            # print(tmp1, tmp2)
            # break

            c1 = tmp1
            c2 = tmp2

        
