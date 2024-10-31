# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        def call(l, r):
            if l > r:
                return None

            m = (l + r) // 2

            curr = TreeNode(res[m])
            curr.left = call(l, m-1)
            curr.right = call(m+1, r)

            return curr
        
        return call(0, len(res) - 1)