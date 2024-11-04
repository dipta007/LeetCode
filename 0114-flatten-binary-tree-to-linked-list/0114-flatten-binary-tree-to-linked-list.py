# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten(node):
            if not node:
                return None

            if not node.left and not node.right:
                return node

            lft_tail = flatten(node.left)
            rgt_tail = flatten(node.right)

            if lft_tail:
                lft_tail.right = node.right
                node.right = node.left
                node.left = None
            
            return rgt_tail if rgt_tail else lft_tail

        flatten(root)

            