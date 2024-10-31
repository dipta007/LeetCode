# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        mn = float('inf')
        res = -1
        def call(curr):
            if not curr:
                return
            
            call(curr.left)
            call(curr.right)
            nonlocal mn, res
            if abs(curr.val - target) < mn:
                mn = abs(curr.val - target)
                res = curr.val
            elif abs(curr.val - target) == mn and curr.val < res:
                res = curr.val
        
        call(root)
        return res

