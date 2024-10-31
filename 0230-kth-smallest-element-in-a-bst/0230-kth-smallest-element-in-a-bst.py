# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = -1
        def call(curr):
            if not curr:
                return
            
            call(curr.left)
            nonlocal cnt, res
            cnt += 1
            if cnt == k:
                res = curr.val
            call(curr.right)
        
        call(root)
        return res