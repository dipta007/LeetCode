# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def call(curr):
            if not curr:
                return float('inf'), float('-inf'), 0

            lft = call(curr.left)
            rgt = call(curr.right)

            if lft[1] < curr.val < rgt[0]:
                return min(lft[0], curr.val), max(rgt[1], curr.val), lft[2] + rgt[2] + 1
            
            return float('-inf'), float('inf'), max(lft[2], rgt[2])

        return call(root)[2]
            
