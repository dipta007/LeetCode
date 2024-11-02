# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(curr):
            if curr is None:
                return None

            if p.val < curr.val and q.val < curr.val:
                return lca(curr.left)
            elif p.val > curr.val and q.val > curr.val:
                return lca(curr.right)
            else:
                return curr

        return lca(root)