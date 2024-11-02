# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def lca(curr):
            if curr is None:
                return 0
            
            tot = 0

            if p.val <= curr.val or q.val <= curr.val:
                tot += lca(curr.left)
            if p.val > curr.val or q.val > curr.val:
                tot += lca(curr.right)

            tot += int(curr == p or curr == q)

            nonlocal res
            if tot == 2 and res is None:
                res = curr

            return tot

        lca(root)
        return res