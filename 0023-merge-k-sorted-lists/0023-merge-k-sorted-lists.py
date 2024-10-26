# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ind = [c for c in lists]

        head = ListNode(0)
        res = head
        while True:
            mn, mn_ind = float('inf'), -1
            for i, c in enumerate(ind):
                if c and c.val < mn:
                    mn = c.val
                    mn_ind = i
            
            if mn_ind == -1:
                break
            res.next = ListNode(mn)
            res = res.next
            ind[mn_ind] = ind[mn_ind].next
        
        return head.next
            
