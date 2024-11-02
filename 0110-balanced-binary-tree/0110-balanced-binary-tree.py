# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def call(curr):
            if curr is None:
                return 0
            
            lft = call(curr.left)
            rgt = call(curr.right)

            if abs(rgt - lft) > 1:
                nonlocal res
                res = False
            
            return max(lft, rgt) + 1

        call(root)
        return res