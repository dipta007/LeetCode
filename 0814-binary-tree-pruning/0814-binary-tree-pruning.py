# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def call(curr):
            if curr is None:
                return 0

            lft = call(curr.left)
            if lft == 0:
                curr.left = None
            
            rgt = call(curr.right)
            if rgt == 0:
                curr.right = None
            
            return lft + rgt + curr.val

        val = call(root)
        if val == 0: return
        return root