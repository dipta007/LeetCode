# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def call(curr):
            if curr == p or curr == q:
                return curr
            if curr:
                lft = call(curr.left)
                rgt = call(curr.right)

                if lft and rgt:
                    return curr
                
                return lft if lft is not None else rgt
        
        return call(root)