# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def is_leaf(curr):
            return not (curr.left or curr.right)
        
        res = 0
        def call(curr, num):
            if not curr:
                return
            
            nonlocal res
            if is_leaf(curr):
                res += (num*10 + curr.val)
            else:
                call(curr.left, num*10+curr.val)
                call(curr.right, num*10+curr.val)

        
        call(root, 0)
        return res