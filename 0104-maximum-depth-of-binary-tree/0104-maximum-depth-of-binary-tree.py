# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def call(curr):
            if curr is None:
                return 0

            lft = call(curr.left)
            rgt = call(curr.right)

            return max(lft, rgt) + 1

        return call(root)