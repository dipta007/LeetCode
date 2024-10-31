# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def call(node):
            if node:
                call(node.left)
                nonlocal res
                res.append(node.val)
                call(node.right)
            
        call(root)
        return res