# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(lft, rgt, curr):
            if curr is None:
                return True

            if curr.val < lft or curr.val > rgt:
                return False
            
            return check(lft, curr.val-1, curr.left) and check(curr.val+1, rgt, curr.right)

        return check(-int(2147483655), int(2147483655), root)