# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def call(curr):
            if not curr:
                return 0

            res = curr.val if (low <= curr.val <= high) else 0

            res += call(curr.left)
            res += call(curr.right)

            return res
        
        return call(root)