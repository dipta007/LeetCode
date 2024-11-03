# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def call(curr):
            if not curr:
                return False

            lft = call(curr.left)
            rgt = call(curr.right)

            tot = int(curr == p or curr == q) + int(lft) + int(rgt)
            if tot == 2:
                nonlocal res
                res = curr

            return tot > 0
        
        call(root)
        return res
