# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        def call(curr):
            if not curr:
                return 0
            
            lft = call(curr.left)
            rgt = call(curr.right)
            nonlocal res
            res = max(res, lft + rgt)

            return max(lft + 1, rgt + 1)
        
        call(root)
        return res