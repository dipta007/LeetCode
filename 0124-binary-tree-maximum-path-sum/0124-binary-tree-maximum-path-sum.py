# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def call(curr):
            if curr is None:
                return float('-inf')
            
            lft = call(curr.left)
            rgt = call(curr.right)

            o1 = (0 if lft == float('-inf') else lft)
            o1 += (0 if rgt == float('-inf') else rgt)
            o1 += curr.val

            o2 = (0 if lft == float('-inf') else lft)
            o2 += curr.val

            o3 = (0 if rgt == float('-inf') else rgt)
            o3 += curr.val

            nonlocal res
            res = max(res, o1, o2, o3, lft, rgt, curr.val)

            return max(o2, o3, curr.val)

        call(root)
        return res